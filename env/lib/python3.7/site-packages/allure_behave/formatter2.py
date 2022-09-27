from behave.model import ScenarioOutline
from behave.formatter.base import Formatter
import allure_commons
from allure_commons.logger import AllureFileLogger
# from allure_behave.listener import AllureListener
from allure_commons.reporter import AllureReporter

from collections import deque
import allure_commons
from allure_commons.reporter import AllureReporter
from allure_commons.utils import uuid4
from allure_commons.utils import now
from allure_commons.utils import platform_label
from allure_commons.types import LabelType, AttachmentType
from allure_commons.model2 import TestResult
from allure_commons.model2 import TestStepResult
from allure_commons.model2 import TestBeforeResult, TestAfterResult
from allure_commons.model2 import TestResultContainer
from allure_commons.model2 import Parameter, Label

from allure_behave.utils import scenario_parameters
from allure_behave.utils import scenario_severity
from allure_behave.utils import scenario_tags
from allure_behave.utils import scenario_name
from allure_behave.utils import scenario_history_id
from allure_behave.utils import step_status, step_status_details
from allure_behave.utils import scenario_status, scenario_status_details
from allure_behave.utils import step_table
from allure_behave.utils import get_status, get_status_details


class AllureFormatter(Formatter):
    def __init__(self, stream_opener, config):
        super(AllureFormatter, self).__init__(stream_opener, config)

        # assert False, stream_opener.name

        self.allure_listener = AllureBehaveListener()
        allure_commons.plugin_manager.register(self.allure_listener)

        file_logger = AllureFileLogger(self.stream_opener.name)
        allure_commons.plugin_manager.register(file_logger)

        self.processed_scenario = None

    def feature(self, feature):
        with open("/tmp/ass.txt", mode="w") as f:
            f.write("we")
            f.write("!!! %s" % feature.name)

    def scenario(self, scenario):

        if self.processed_scenario:
            self.allure_listener.after_scenario(self.processed_scenario)

        self.processed_scenario = scenario
        self.allure_listener.before_scenario(self.processed_scenario)

    def eof(self):

        if self.processed_scenario:
            self.allure_listener.after_scenario(self.processed_scenario)

        self.processed_scenario = None


import mock
import behave


def f(self, name, context, *args):
    print("-------")
    print(name)
    print("-------")



class AllureNinjaFormatter(Formatter):
    def __init__(self, stream_opener, config):
        patcher = mock.patch('behave.runner.ModelRunner')
        MockClass = patcher.start()
        ins = MockClass()
        assert False, dir(ins.run_hook)


    def close(self):
        pass


class AllureBehaveListener(object):
    def __init__(self):
        self.allure_lifecycle = AllureReporter()

    def before_scenario(self, _, scenario):
        uuid = scenario_history_id(scenario)

        test_case = TestResult(uuid=uuid, start=now())
        test_case.name = scenario_name(scenario)
        test_case.historyId = scenario_history_id(scenario)

        self.allure_lifecycle.schedule_test(uuid, test_case)

    def after_scenario(self, _, scenario):
        uuid = scenario_history_id(scenario)
        self.allure_lifecycle.close_test(uuid)
