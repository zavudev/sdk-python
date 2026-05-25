# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    FunctionCreateResponse,
    FunctionDeleteResponse,
    FunctionDeployResponse,
    FunctionUpdateResponse,
    FunctionRetrieveResponse,
    FunctionTailLogsResponse,
    FunctionGetDeploymentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        function = client.functions.create(
            name="Order Bot",
            slug="order-bot",
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        function = client.functions.create(
            name="Order Bot",
            slug="order-bot",
            dependencies={"openai": "^4.20.0"},
            description="Replies to order status questions on WhatsApp.",
            http_enabled=True,
            memory_mb=128,
            runtime="nodejs24",
            source_code="import { defineFunction } from '@zavu/functions';\n\nexport default defineFunction(async (event, ctx) => {\n  ctx.log('received', event.type);\n});\n",
            timeout_sec=1,
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.functions.with_raw_response.create(
            name="Order Bot",
            slug="order-bot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.functions.with_streaming_response.create(
            name="Order Bot",
            slug="order-bot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionCreateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        function = client.functions.retrieve(
            "functionId",
        )
        assert_matches_type(FunctionRetrieveResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.functions.with_raw_response.retrieve(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionRetrieveResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.functions.with_streaming_response.retrieve(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionRetrieveResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        function = client.functions.update(
            function_id="functionId",
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        function = client.functions.update(
            function_id="functionId",
            dependencies={"foo": "string"},
            source_code="sourceCode",
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.functions.with_raw_response.update(
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.functions.with_streaming_response.update(
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionUpdateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.with_raw_response.update(
                function_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        function = client.functions.delete(
            "functionId",
        )
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.functions.with_raw_response.delete(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.functions.with_streaming_response.delete(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionDeleteResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deploy(self, client: Zavudev) -> None:
        function = client.functions.deploy(
            function_id="functionId",
        )
        assert_matches_type(FunctionDeployResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deploy_with_all_params(self, client: Zavudev) -> None:
        function = client.functions.deploy(
            function_id="functionId",
            dependencies={"foo": "string"},
            source_code="sourceCode",
        )
        assert_matches_type(FunctionDeployResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deploy(self, client: Zavudev) -> None:
        response = client.functions.with_raw_response.deploy(
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionDeployResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deploy(self, client: Zavudev) -> None:
        with client.functions.with_streaming_response.deploy(
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionDeployResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deploy(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.with_raw_response.deploy(
                function_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_deployment(self, client: Zavudev) -> None:
        function = client.functions.get_deployment(
            "deploymentId",
        )
        assert_matches_type(FunctionGetDeploymentResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_deployment(self, client: Zavudev) -> None:
        response = client.functions.with_raw_response.get_deployment(
            "deploymentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionGetDeploymentResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_deployment(self, client: Zavudev) -> None:
        with client.functions.with_streaming_response.get_deployment(
            "deploymentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionGetDeploymentResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_deployment(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.functions.with_raw_response.get_deployment(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_tail_logs(self, client: Zavudev) -> None:
        function = client.functions.tail_logs(
            function_id="functionId",
        )
        assert_matches_type(FunctionTailLogsResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_tail_logs_with_all_params(self, client: Zavudev) -> None:
        function = client.functions.tail_logs(
            function_id="functionId",
            end_time=0,
            filter_pattern="filterPattern",
            limit=1,
            next_token="nextToken",
            start_time=0,
        )
        assert_matches_type(FunctionTailLogsResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_tail_logs(self, client: Zavudev) -> None:
        response = client.functions.with_raw_response.tail_logs(
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionTailLogsResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_tail_logs(self, client: Zavudev) -> None:
        with client.functions.with_streaming_response.tail_logs(
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionTailLogsResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_tail_logs(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.with_raw_response.tail_logs(
                function_id="",
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.create(
            name="Order Bot",
            slug="order-bot",
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.create(
            name="Order Bot",
            slug="order-bot",
            dependencies={"openai": "^4.20.0"},
            description="Replies to order status questions on WhatsApp.",
            http_enabled=True,
            memory_mb=128,
            runtime="nodejs24",
            source_code="import { defineFunction } from '@zavu/functions';\n\nexport default defineFunction(async (event, ctx) => {\n  ctx.log('received', event.type);\n});\n",
            timeout_sec=1,
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.with_raw_response.create(
            name="Order Bot",
            slug="order-bot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.with_streaming_response.create(
            name="Order Bot",
            slug="order-bot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionCreateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.retrieve(
            "functionId",
        )
        assert_matches_type(FunctionRetrieveResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.with_raw_response.retrieve(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionRetrieveResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.with_streaming_response.retrieve(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionRetrieveResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.update(
            function_id="functionId",
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.update(
            function_id="functionId",
            dependencies={"foo": "string"},
            source_code="sourceCode",
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.with_raw_response.update(
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.with_streaming_response.update(
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionUpdateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.with_raw_response.update(
                function_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.delete(
            "functionId",
        )
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.with_raw_response.delete(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.with_streaming_response.delete(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionDeleteResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deploy(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.deploy(
            function_id="functionId",
        )
        assert_matches_type(FunctionDeployResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deploy_with_all_params(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.deploy(
            function_id="functionId",
            dependencies={"foo": "string"},
            source_code="sourceCode",
        )
        assert_matches_type(FunctionDeployResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deploy(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.with_raw_response.deploy(
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionDeployResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deploy(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.with_streaming_response.deploy(
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionDeployResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deploy(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.with_raw_response.deploy(
                function_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_deployment(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.get_deployment(
            "deploymentId",
        )
        assert_matches_type(FunctionGetDeploymentResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_deployment(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.with_raw_response.get_deployment(
            "deploymentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionGetDeploymentResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_deployment(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.with_streaming_response.get_deployment(
            "deploymentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionGetDeploymentResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_deployment(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.functions.with_raw_response.get_deployment(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_tail_logs(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.tail_logs(
            function_id="functionId",
        )
        assert_matches_type(FunctionTailLogsResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_tail_logs_with_all_params(self, async_client: AsyncZavudev) -> None:
        function = await async_client.functions.tail_logs(
            function_id="functionId",
            end_time=0,
            filter_pattern="filterPattern",
            limit=1,
            next_token="nextToken",
            start_time=0,
        )
        assert_matches_type(FunctionTailLogsResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_tail_logs(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.with_raw_response.tail_logs(
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionTailLogsResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_tail_logs(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.with_streaming_response.tail_logs(
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionTailLogsResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_tail_logs(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.with_raw_response.tail_logs(
                function_id="",
            )
