import urllib

import requests
from logging import getLogger

from notebooker.web.app import GLOBAL_CONFIG

logger = getLogger(__name__)


def run_report(report_name: str, overrides: dict, report_title: str, mailto: str, generate_pdf: bool, hide_code: bool):
    url = f"http://localhost:{GLOBAL_CONFIG.PORT}/run_report_json/{report_name}"
    payload = {
        "overrides": overrides,
        "report_title": report_title,
        "mailto": mailto,
        "generate_pdf": generate_pdf,
        "hide_code": hide_code,
    }
    logger.info(f"Running report at {url}, payload = {payload}")
    result = requests.post(url, params=urllib.parse.urlencode(payload))
    logger.info(result.content)
    result.raise_for_status()