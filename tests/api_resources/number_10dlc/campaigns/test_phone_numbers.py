# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types.number_10dlc.campaigns import (
    PhoneNumberListResponse,
    PhoneNumberAssignResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        phone_number = client.number_10dlc.campaigns.phone_numbers.list(
            "campaignId",
        )
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.number_10dlc.campaigns.phone_numbers.with_raw_response.list(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.number_10dlc.campaigns.phone_numbers.with_streaming_response.list(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaigns.phone_numbers.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_assign(self, client: Zavudev) -> None:
        phone_number = client.number_10dlc.campaigns.phone_numbers.assign(
            campaign_id="campaignId",
            phone_number_id="pn_abc123",
        )
        assert_matches_type(PhoneNumberAssignResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_assign(self, client: Zavudev) -> None:
        response = client.number_10dlc.campaigns.phone_numbers.with_raw_response.assign(
            campaign_id="campaignId",
            phone_number_id="pn_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberAssignResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_assign(self, client: Zavudev) -> None:
        with client.number_10dlc.campaigns.phone_numbers.with_streaming_response.assign(
            campaign_id="campaignId",
            phone_number_id="pn_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberAssignResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_assign(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaigns.phone_numbers.with_raw_response.assign(
                campaign_id="",
                phone_number_id="pn_abc123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unassign(self, client: Zavudev) -> None:
        phone_number = client.number_10dlc.campaigns.phone_numbers.unassign(
            assignment_id="assignmentId",
            campaign_id="campaignId",
        )
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unassign(self, client: Zavudev) -> None:
        response = client.number_10dlc.campaigns.phone_numbers.with_raw_response.unassign(
            assignment_id="assignmentId",
            campaign_id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unassign(self, client: Zavudev) -> None:
        with client.number_10dlc.campaigns.phone_numbers.with_streaming_response.unassign(
            assignment_id="assignmentId",
            campaign_id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert phone_number is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unassign(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaigns.phone_numbers.with_raw_response.unassign(
                assignment_id="assignmentId",
                campaign_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assignment_id` but received ''"):
            client.number_10dlc.campaigns.phone_numbers.with_raw_response.unassign(
                assignment_id="",
                campaign_id="campaignId",
            )


class TestAsyncPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.number_10dlc.campaigns.phone_numbers.list(
            "campaignId",
        )
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.campaigns.phone_numbers.with_raw_response.list(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.campaigns.phone_numbers.with_streaming_response.list(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaigns.phone_numbers.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_assign(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.number_10dlc.campaigns.phone_numbers.assign(
            campaign_id="campaignId",
            phone_number_id="pn_abc123",
        )
        assert_matches_type(PhoneNumberAssignResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_assign(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.campaigns.phone_numbers.with_raw_response.assign(
            campaign_id="campaignId",
            phone_number_id="pn_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberAssignResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_assign(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.campaigns.phone_numbers.with_streaming_response.assign(
            campaign_id="campaignId",
            phone_number_id="pn_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberAssignResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_assign(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaigns.phone_numbers.with_raw_response.assign(
                campaign_id="",
                phone_number_id="pn_abc123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unassign(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.number_10dlc.campaigns.phone_numbers.unassign(
            assignment_id="assignmentId",
            campaign_id="campaignId",
        )
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unassign(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.campaigns.phone_numbers.with_raw_response.unassign(
            assignment_id="assignmentId",
            campaign_id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unassign(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.campaigns.phone_numbers.with_streaming_response.unassign(
            assignment_id="assignmentId",
            campaign_id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert phone_number is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unassign(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaigns.phone_numbers.with_raw_response.unassign(
                assignment_id="assignmentId",
                campaign_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assignment_id` but received ''"):
            await async_client.number_10dlc.campaigns.phone_numbers.with_raw_response.unassign(
                assignment_id="",
                campaign_id="campaignId",
            )
