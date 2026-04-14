# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.pagination import SyncCursor, AsyncCursor
from zavudev.types.number_10dlc import (
    TenDlcCampaign,
    CampaignCreateResponse,
    CampaignSubmitResponse,
    CampaignUpdateResponse,
    CampaignRetrieveResponse,
    CampaignSyncStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCampaigns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        campaign = client.number_10dlc.campaigns.create(
            affiliate_marketing=False,
            age_gated=False,
            brand_id="brand_abc123",
            description="Send order status updates and shipping notifications to customers who opted in.",
            direct_lending=False,
            embedded_link=True,
            embedded_phone=False,
            name="Order Notifications",
            number_pooling=False,
            sample_messages=[
                "Hi {{name}}, your order #{{order_id}} has shipped! Track it at {{url}}",
                "Your order #{{order_id}} has been delivered. Thank you for your purchase!",
            ],
            subscriber_help=True,
            subscriber_opt_in=True,
            subscriber_opt_out=True,
            use_case="ACCOUNT_NOTIFICATION",
        )
        assert_matches_type(CampaignCreateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        campaign = client.number_10dlc.campaigns.create(
            affiliate_marketing=False,
            age_gated=False,
            brand_id="brand_abc123",
            description="Send order status updates and shipping notifications to customers who opted in.",
            direct_lending=False,
            embedded_link=True,
            embedded_phone=False,
            name="Order Notifications",
            number_pooling=False,
            sample_messages=[
                "Hi {{name}}, your order #{{order_id}} has shipped! Track it at {{url}}",
                "Your order #{{order_id}} has been delivered. Thank you for your purchase!",
            ],
            subscriber_help=True,
            subscriber_opt_in=True,
            subscriber_opt_out=True,
            use_case="ACCOUNT_NOTIFICATION",
            help_message="helpMessage",
            message_flow="messageFlow",
            opt_in_keywords=["string"],
            opt_out_keywords=["string"],
            sub_use_cases=["string"],
        )
        assert_matches_type(CampaignCreateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.number_10dlc.campaigns.with_raw_response.create(
            affiliate_marketing=False,
            age_gated=False,
            brand_id="brand_abc123",
            description="Send order status updates and shipping notifications to customers who opted in.",
            direct_lending=False,
            embedded_link=True,
            embedded_phone=False,
            name="Order Notifications",
            number_pooling=False,
            sample_messages=[
                "Hi {{name}}, your order #{{order_id}} has shipped! Track it at {{url}}",
                "Your order #{{order_id}} has been delivered. Thank you for your purchase!",
            ],
            subscriber_help=True,
            subscriber_opt_in=True,
            subscriber_opt_out=True,
            use_case="ACCOUNT_NOTIFICATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignCreateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.number_10dlc.campaigns.with_streaming_response.create(
            affiliate_marketing=False,
            age_gated=False,
            brand_id="brand_abc123",
            description="Send order status updates and shipping notifications to customers who opted in.",
            direct_lending=False,
            embedded_link=True,
            embedded_phone=False,
            name="Order Notifications",
            number_pooling=False,
            sample_messages=[
                "Hi {{name}}, your order #{{order_id}} has shipped! Track it at {{url}}",
                "Your order #{{order_id}} has been delivered. Thank you for your purchase!",
            ],
            subscriber_help=True,
            subscriber_opt_in=True,
            subscriber_opt_out=True,
            use_case="ACCOUNT_NOTIFICATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignCreateResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        campaign = client.number_10dlc.campaigns.retrieve(
            "campaignId",
        )
        assert_matches_type(CampaignRetrieveResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.number_10dlc.campaigns.with_raw_response.retrieve(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignRetrieveResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.number_10dlc.campaigns.with_streaming_response.retrieve(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignRetrieveResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaigns.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        campaign = client.number_10dlc.campaigns.update(
            campaign_id="campaignId",
        )
        assert_matches_type(CampaignUpdateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        campaign = client.number_10dlc.campaigns.update(
            campaign_id="campaignId",
            description="description",
            help_message="helpMessage",
            message_flow="messageFlow",
            name="name",
            opt_in_keywords=["string"],
            opt_out_keywords=["string"],
            sample_messages=["string"],
        )
        assert_matches_type(CampaignUpdateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.number_10dlc.campaigns.with_raw_response.update(
            campaign_id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignUpdateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.number_10dlc.campaigns.with_streaming_response.update(
            campaign_id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignUpdateResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaigns.with_raw_response.update(
                campaign_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        campaign = client.number_10dlc.campaigns.list()
        assert_matches_type(SyncCursor[TenDlcCampaign], campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        campaign = client.number_10dlc.campaigns.list(
            brand_id="brandId",
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(SyncCursor[TenDlcCampaign], campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.number_10dlc.campaigns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(SyncCursor[TenDlcCampaign], campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.number_10dlc.campaigns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(SyncCursor[TenDlcCampaign], campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        campaign = client.number_10dlc.campaigns.delete(
            "campaignId",
        )
        assert campaign is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.number_10dlc.campaigns.with_raw_response.delete(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert campaign is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.number_10dlc.campaigns.with_streaming_response.delete(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert campaign is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaigns.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Zavudev) -> None:
        campaign = client.number_10dlc.campaigns.submit(
            "campaignId",
        )
        assert_matches_type(CampaignSubmitResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Zavudev) -> None:
        response = client.number_10dlc.campaigns.with_raw_response.submit(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignSubmitResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Zavudev) -> None:
        with client.number_10dlc.campaigns.with_streaming_response.submit(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignSubmitResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaigns.with_raw_response.submit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync_status(self, client: Zavudev) -> None:
        campaign = client.number_10dlc.campaigns.sync_status(
            "campaignId",
        )
        assert_matches_type(CampaignSyncStatusResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sync_status(self, client: Zavudev) -> None:
        response = client.number_10dlc.campaigns.with_raw_response.sync_status(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignSyncStatusResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sync_status(self, client: Zavudev) -> None:
        with client.number_10dlc.campaigns.with_streaming_response.sync_status(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignSyncStatusResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_sync_status(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaigns.with_raw_response.sync_status(
                "",
            )


class TestAsyncCampaigns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        campaign = await async_client.number_10dlc.campaigns.create(
            affiliate_marketing=False,
            age_gated=False,
            brand_id="brand_abc123",
            description="Send order status updates and shipping notifications to customers who opted in.",
            direct_lending=False,
            embedded_link=True,
            embedded_phone=False,
            name="Order Notifications",
            number_pooling=False,
            sample_messages=[
                "Hi {{name}}, your order #{{order_id}} has shipped! Track it at {{url}}",
                "Your order #{{order_id}} has been delivered. Thank you for your purchase!",
            ],
            subscriber_help=True,
            subscriber_opt_in=True,
            subscriber_opt_out=True,
            use_case="ACCOUNT_NOTIFICATION",
        )
        assert_matches_type(CampaignCreateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        campaign = await async_client.number_10dlc.campaigns.create(
            affiliate_marketing=False,
            age_gated=False,
            brand_id="brand_abc123",
            description="Send order status updates and shipping notifications to customers who opted in.",
            direct_lending=False,
            embedded_link=True,
            embedded_phone=False,
            name="Order Notifications",
            number_pooling=False,
            sample_messages=[
                "Hi {{name}}, your order #{{order_id}} has shipped! Track it at {{url}}",
                "Your order #{{order_id}} has been delivered. Thank you for your purchase!",
            ],
            subscriber_help=True,
            subscriber_opt_in=True,
            subscriber_opt_out=True,
            use_case="ACCOUNT_NOTIFICATION",
            help_message="helpMessage",
            message_flow="messageFlow",
            opt_in_keywords=["string"],
            opt_out_keywords=["string"],
            sub_use_cases=["string"],
        )
        assert_matches_type(CampaignCreateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.campaigns.with_raw_response.create(
            affiliate_marketing=False,
            age_gated=False,
            brand_id="brand_abc123",
            description="Send order status updates and shipping notifications to customers who opted in.",
            direct_lending=False,
            embedded_link=True,
            embedded_phone=False,
            name="Order Notifications",
            number_pooling=False,
            sample_messages=[
                "Hi {{name}}, your order #{{order_id}} has shipped! Track it at {{url}}",
                "Your order #{{order_id}} has been delivered. Thank you for your purchase!",
            ],
            subscriber_help=True,
            subscriber_opt_in=True,
            subscriber_opt_out=True,
            use_case="ACCOUNT_NOTIFICATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignCreateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.campaigns.with_streaming_response.create(
            affiliate_marketing=False,
            age_gated=False,
            brand_id="brand_abc123",
            description="Send order status updates and shipping notifications to customers who opted in.",
            direct_lending=False,
            embedded_link=True,
            embedded_phone=False,
            name="Order Notifications",
            number_pooling=False,
            sample_messages=[
                "Hi {{name}}, your order #{{order_id}} has shipped! Track it at {{url}}",
                "Your order #{{order_id}} has been delivered. Thank you for your purchase!",
            ],
            subscriber_help=True,
            subscriber_opt_in=True,
            subscriber_opt_out=True,
            use_case="ACCOUNT_NOTIFICATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignCreateResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        campaign = await async_client.number_10dlc.campaigns.retrieve(
            "campaignId",
        )
        assert_matches_type(CampaignRetrieveResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.campaigns.with_raw_response.retrieve(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignRetrieveResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.campaigns.with_streaming_response.retrieve(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignRetrieveResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaigns.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        campaign = await async_client.number_10dlc.campaigns.update(
            campaign_id="campaignId",
        )
        assert_matches_type(CampaignUpdateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        campaign = await async_client.number_10dlc.campaigns.update(
            campaign_id="campaignId",
            description="description",
            help_message="helpMessage",
            message_flow="messageFlow",
            name="name",
            opt_in_keywords=["string"],
            opt_out_keywords=["string"],
            sample_messages=["string"],
        )
        assert_matches_type(CampaignUpdateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.campaigns.with_raw_response.update(
            campaign_id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignUpdateResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.campaigns.with_streaming_response.update(
            campaign_id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignUpdateResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaigns.with_raw_response.update(
                campaign_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        campaign = await async_client.number_10dlc.campaigns.list()
        assert_matches_type(AsyncCursor[TenDlcCampaign], campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        campaign = await async_client.number_10dlc.campaigns.list(
            brand_id="brandId",
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(AsyncCursor[TenDlcCampaign], campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.campaigns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(AsyncCursor[TenDlcCampaign], campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.campaigns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(AsyncCursor[TenDlcCampaign], campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        campaign = await async_client.number_10dlc.campaigns.delete(
            "campaignId",
        )
        assert campaign is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.campaigns.with_raw_response.delete(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert campaign is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.campaigns.with_streaming_response.delete(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert campaign is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaigns.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncZavudev) -> None:
        campaign = await async_client.number_10dlc.campaigns.submit(
            "campaignId",
        )
        assert_matches_type(CampaignSubmitResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.campaigns.with_raw_response.submit(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignSubmitResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.campaigns.with_streaming_response.submit(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignSubmitResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaigns.with_raw_response.submit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync_status(self, async_client: AsyncZavudev) -> None:
        campaign = await async_client.number_10dlc.campaigns.sync_status(
            "campaignId",
        )
        assert_matches_type(CampaignSyncStatusResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sync_status(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.campaigns.with_raw_response.sync_status(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignSyncStatusResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sync_status(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.campaigns.with_streaming_response.sync_status(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignSyncStatusResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_sync_status(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaigns.with_raw_response.sync_status(
                "",
            )
