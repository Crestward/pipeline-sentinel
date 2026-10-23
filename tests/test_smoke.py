from warehouse_graph.llm import FakeProvider, LLMRequest

import pipeline_sentinel


def test_package_imports() -> None:
    assert pipeline_sentinel.__version__ == "0.1.0"


def test_shared_llm_layer_is_available() -> None:
    request = LLMRequest(
        model="claude-sonnet-5-5",
        max_tokens=8,
        call_site="pipeline_sentinel.smoke",
        messages=[{"role": "user", "content": "hi"}],
    )
    assert FakeProvider().complete(request).text == "fake:pipeline_sentinel.smoke"
