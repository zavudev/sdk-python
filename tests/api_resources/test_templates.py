# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    Template,
)
from zavudev.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        template = client.templates.create(
            body="Hi {{1}}, your order {{2}} has been confirmed and will ship within 24 hours.",
            language="en",
            name="order_confirmation",
        )
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        template = client.templates.create(
            body="Hi {{1}}, your order {{2}} has been confirmed and will ship within 24 hours.",
            language="en",
            name="order_confirmation",
            add_security_recommendation=True,
            buttons=[
                {
                    "text": "text",
                    "type": "quick_reply",
                    "otp_type": "COPY_CODE",
                    "package_name": "packageName",
                    "phone_number": "phoneNumber",
                    "signature_hash": "signatureHash",
                    "url": "https://example.com",
                }
            ],
            code_expiration_minutes=1,
            variables=["customer_name", "order_id"],
            whatsapp_category="UTILITY",
        )
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.templates.with_raw_response.create(
            body="Hi {{1}}, your order {{2}} has been confirmed and will ship within 24 hours.",
            language="en",
            name="order_confirmation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.templates.with_streaming_response.create(
            body="Hi {{1}}, your order {{2}} has been confirmed and will ship within 24 hours.",
            language="en",
            name="order_confirmation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(Template, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        template = client.templates.retrieve(
            "templateId",
        )
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.templates.with_raw_response.retrieve(
            "templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.templates.with_streaming_response.retrieve(
            "templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(Template, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.templates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        template = client.templates.list()
        assert_matches_type(SyncCursor[Template], template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        template = client.templates.list(
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(SyncCursor[Template], template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(SyncCursor[Template], template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(SyncCursor[Template], template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        template = client.templates.delete(
            "templateId",
        )
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.templates.with_raw_response.delete(
            "templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.templates.with_streaming_response.delete(
            "templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.templates.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit(self, client: Zavudev) -> None:
        template = client.templates.submit(
            template_id="templateId",
            sender_id="sender_abc123",
        )
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: Zavudev) -> None:
        template = client.templates.submit(
            template_id="templateId",
            sender_id="sender_abc123",
            category="UTILITY",
        )
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Zavudev) -> None:
        response = client.templates.with_raw_response.submit(
            template_id="templateId",
            sender_id="sender_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Zavudev) -> None:
        with client.templates.with_streaming_response.submit(
            template_id="templateId",
            sender_id="sender_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(Template, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.templates.with_raw_response.submit(
                template_id="",
                sender_id="sender_abc123",
            )


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        template = await async_client.templates.create(
            body="Hi {{1}}, your order {{2}} has been confirmed and will ship within 24 hours.",
            language="en",
            name="order_confirmation",
        )
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        template = await async_client.templates.create(
            body="Hi {{1}}, your order {{2}} has been confirmed and will ship within 24 hours.",
            language="en",
            name="order_confirmation",
            add_security_recommendation=True,
            buttons=[
                {
                    "text": "text",
                    "type": "quick_reply",
                    "otp_type": "COPY_CODE",
                    "package_name": "packageName",
                    "phone_number": "phoneNumber",
                    "signature_hash": "signatureHash",
                    "url": "https://example.com",
                }
            ],
            code_expiration_minutes=1,
            variables=["customer_name", "order_id"],
            whatsapp_category="UTILITY",
        )
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.templates.with_raw_response.create(
            body="Hi {{1}}, your order {{2}} has been confirmed and will ship within 24 hours.",
            language="en",
            name="order_confirmation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.templates.with_streaming_response.create(
            body="Hi {{1}}, your order {{2}} has been confirmed and will ship within 24 hours.",
            language="en",
            name="order_confirmation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(Template, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        template = await async_client.templates.retrieve(
            "templateId",
        )
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.templates.with_raw_response.retrieve(
            "templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.templates.with_streaming_response.retrieve(
            "templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(Template, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.templates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        template = await async_client.templates.list()
        assert_matches_type(AsyncCursor[Template], template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        template = await async_client.templates.list(
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(AsyncCursor[Template], template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(AsyncCursor[Template], template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(AsyncCursor[Template], template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        template = await async_client.templates.delete(
            "templateId",
        )
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.templates.with_raw_response.delete(
            "templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.templates.with_streaming_response.delete(
            "templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.templates.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncZavudev) -> None:
        template = await async_client.templates.submit(
            template_id="templateId",
            sender_id="sender_abc123",
        )
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncZavudev) -> None:
        template = await async_client.templates.submit(
            template_id="templateId",
            sender_id="sender_abc123",
            category="UTILITY",
        )
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncZavudev) -> None:
        response = await async_client.templates.with_raw_response.submit(
            template_id="templateId",
            sender_id="sender_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(Template, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncZavudev) -> None:
        async with async_client.templates.with_streaming_response.submit(
            template_id="templateId",
            sender_id="sender_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(Template, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.templates.with_raw_response.submit(
                template_id="",
                sender_id="sender_abc123",
            )
