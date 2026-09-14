# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types.functions import (
    GitLinkLinkResponse,
    GitLinkUpdateResponse,
    GitLinkRetrieveResponse,
    GitLinkDeployNowResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGitLink:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        git_link = client.functions.git_link.retrieve(
            "functionId",
        )
        assert_matches_type(GitLinkRetrieveResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.functions.git_link.with_raw_response.retrieve(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_link = response.parse()
        assert_matches_type(GitLinkRetrieveResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.functions.git_link.with_streaming_response.retrieve(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_link = response.parse()
            assert_matches_type(GitLinkRetrieveResponse, git_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.git_link.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        git_link = client.functions.git_link.update(
            function_id="functionId",
        )
        assert_matches_type(GitLinkUpdateResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        git_link = client.functions.git_link.update(
            function_id="functionId",
            auto_deploy=False,
            branch="branch",
            root_dir="rootDir",
        )
        assert_matches_type(GitLinkUpdateResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.functions.git_link.with_raw_response.update(
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_link = response.parse()
        assert_matches_type(GitLinkUpdateResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.functions.git_link.with_streaming_response.update(
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_link = response.parse()
            assert_matches_type(GitLinkUpdateResponse, git_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.git_link.with_raw_response.update(
                function_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deploy_now(self, client: Zavudev) -> None:
        git_link = client.functions.git_link.deploy_now(
            "functionId",
        )
        assert_matches_type(GitLinkDeployNowResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deploy_now(self, client: Zavudev) -> None:
        response = client.functions.git_link.with_raw_response.deploy_now(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_link = response.parse()
        assert_matches_type(GitLinkDeployNowResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deploy_now(self, client: Zavudev) -> None:
        with client.functions.git_link.with_streaming_response.deploy_now(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_link = response.parse()
            assert_matches_type(GitLinkDeployNowResponse, git_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deploy_now(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.git_link.with_raw_response.deploy_now(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_link(self, client: Zavudev) -> None:
        git_link = client.functions.git_link.link(
            function_id="functionId",
            owner="acme",
            repo="order-bot",
        )
        assert_matches_type(GitLinkLinkResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_link_with_all_params(self, client: Zavudev) -> None:
        git_link = client.functions.git_link.link(
            function_id="functionId",
            owner="acme",
            repo="order-bot",
            auto_deploy=True,
            branch="main",
            root_dir="apps/bot",
        )
        assert_matches_type(GitLinkLinkResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_link(self, client: Zavudev) -> None:
        response = client.functions.git_link.with_raw_response.link(
            function_id="functionId",
            owner="acme",
            repo="order-bot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_link = response.parse()
        assert_matches_type(GitLinkLinkResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_link(self, client: Zavudev) -> None:
        with client.functions.git_link.with_streaming_response.link(
            function_id="functionId",
            owner="acme",
            repo="order-bot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_link = response.parse()
            assert_matches_type(GitLinkLinkResponse, git_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_link(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.git_link.with_raw_response.link(
                function_id="",
                owner="acme",
                repo="order-bot",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unlink(self, client: Zavudev) -> None:
        git_link = client.functions.git_link.unlink(
            "functionId",
        )
        assert git_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unlink(self, client: Zavudev) -> None:
        response = client.functions.git_link.with_raw_response.unlink(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_link = response.parse()
        assert git_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unlink(self, client: Zavudev) -> None:
        with client.functions.git_link.with_streaming_response.unlink(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_link = response.parse()
            assert git_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unlink(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.git_link.with_raw_response.unlink(
                "",
            )


class TestAsyncGitLink:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        git_link = await async_client.functions.git_link.retrieve(
            "functionId",
        )
        assert_matches_type(GitLinkRetrieveResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.git_link.with_raw_response.retrieve(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_link = await response.parse()
        assert_matches_type(GitLinkRetrieveResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.git_link.with_streaming_response.retrieve(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_link = await response.parse()
            assert_matches_type(GitLinkRetrieveResponse, git_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.git_link.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        git_link = await async_client.functions.git_link.update(
            function_id="functionId",
        )
        assert_matches_type(GitLinkUpdateResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        git_link = await async_client.functions.git_link.update(
            function_id="functionId",
            auto_deploy=False,
            branch="branch",
            root_dir="rootDir",
        )
        assert_matches_type(GitLinkUpdateResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.git_link.with_raw_response.update(
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_link = await response.parse()
        assert_matches_type(GitLinkUpdateResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.git_link.with_streaming_response.update(
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_link = await response.parse()
            assert_matches_type(GitLinkUpdateResponse, git_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.git_link.with_raw_response.update(
                function_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deploy_now(self, async_client: AsyncZavudev) -> None:
        git_link = await async_client.functions.git_link.deploy_now(
            "functionId",
        )
        assert_matches_type(GitLinkDeployNowResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deploy_now(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.git_link.with_raw_response.deploy_now(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_link = await response.parse()
        assert_matches_type(GitLinkDeployNowResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deploy_now(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.git_link.with_streaming_response.deploy_now(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_link = await response.parse()
            assert_matches_type(GitLinkDeployNowResponse, git_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deploy_now(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.git_link.with_raw_response.deploy_now(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_link(self, async_client: AsyncZavudev) -> None:
        git_link = await async_client.functions.git_link.link(
            function_id="functionId",
            owner="acme",
            repo="order-bot",
        )
        assert_matches_type(GitLinkLinkResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_link_with_all_params(self, async_client: AsyncZavudev) -> None:
        git_link = await async_client.functions.git_link.link(
            function_id="functionId",
            owner="acme",
            repo="order-bot",
            auto_deploy=True,
            branch="main",
            root_dir="apps/bot",
        )
        assert_matches_type(GitLinkLinkResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_link(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.git_link.with_raw_response.link(
            function_id="functionId",
            owner="acme",
            repo="order-bot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_link = await response.parse()
        assert_matches_type(GitLinkLinkResponse, git_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_link(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.git_link.with_streaming_response.link(
            function_id="functionId",
            owner="acme",
            repo="order-bot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_link = await response.parse()
            assert_matches_type(GitLinkLinkResponse, git_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_link(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.git_link.with_raw_response.link(
                function_id="",
                owner="acme",
                repo="order-bot",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unlink(self, async_client: AsyncZavudev) -> None:
        git_link = await async_client.functions.git_link.unlink(
            "functionId",
        )
        assert git_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unlink(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.git_link.with_raw_response.unlink(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_link = await response.parse()
        assert git_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unlink(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.git_link.with_streaming_response.unlink(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_link = await response.parse()
            assert git_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unlink(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.git_link.with_raw_response.unlink(
                "",
            )
