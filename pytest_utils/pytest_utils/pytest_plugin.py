import pytest
import json


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    x = yield
    x._result.max_score = getattr(item._obj, 'max_score', 0)
    x._result.visibility = getattr(item._obj, 'visibility', 'visible')

def pytest_terminal_summary(terminalreporter, exitstatus):
    json_results = {
        'output': 'Text relevant to the entire submission',
        'output_format': 'simple_format',
        'test_output_format': 'text',
        'test_name_format': 'text',
        'stdout_visibility': 'hidden',
        'visibility': 'visible',
        'extra_data': {},
        'tests': []
    }

    all_tests = []
    total_obtained_score = 0
    total_max_score = 0

    if ('passed' in terminalreporter.stats):
        all_tests = all_tests + terminalreporter.stats['passed']
    if ('failed' in terminalreporter.stats):
        all_tests = all_tests + terminalreporter.stats['failed']

    # First, calculate total scores
    for s in all_tests:
        total_max_score += s.max_score
        if s.outcome == 'passed':
            total_obtained_score += s.max_score

    for s in all_tests:
        output = ''
        rescaled_score = 0
        score = s.max_score
        if (s.outcome == 'failed'):
            error_message = str(s.longrepr.reprcrash.message)
            output = error_message
            score = 0
            status = 'failed'  # not sure if needed
        elif (s.outcome == 'passed'):
            rescaled_score = (s.max_score / total_max_score) * 100
            status = 'passed'
        else:
            output = ''
            status = 'failed'

        json_results["tests"].append(
            {
                'score': rescaled_score,
                'non-scaled_score': score,
                'max_score': s.max_score,
                'name': s.location[2],
                'output': output,
                'visibility': s.visibility,
                'status': status
            }
        )

    with open('results.json', 'w') as results:
        results.write(json.dumps(json_results, indent=4))
