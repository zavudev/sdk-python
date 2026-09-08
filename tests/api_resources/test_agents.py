# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    AgentTestResponse,
    AgentCreateResponse,
    AgentUpdateResponse,
    AgentRetrieveResponse,
    AgentListVoicesResponse,
)
from zavudev.pagination import SyncCursor, AsyncCursor
from zavudev.types.senders.agent import Agent

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        agent = client.agents.create(
            model="model",
            name="name",
            provider="openai",
            system_prompt="systemPrompt",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        agent = client.agents.create(
            model="model",
            name="name",
            provider="openai",
            system_prompt="systemPrompt",
            context_window_messages=1,
            include_contact_metadata=True,
            max_tokens=1,
            temperature=0,
            trigger_on_channels=["string"],
            trigger_on_message_types=["string"],
            voice={
                "enabled": True,
                "greeting": "Hi, thanks for calling Acme. How can I help you today?",
                "greetings": {"es": "Hola, soy Atlas. Preguntame lo que quieras."},
                "interruptible": True,
                "language": "en",
                "max_call_duration_minutes": 1,
                "max_idle_seconds": 5,
                "model": "openai/gpt-4o",
                "record_calls": True,
                "stt_model": "sttModel",
                "stt_provider": "sttProvider",
                "transfer_phone_number": "+14155551234",
                "tts_provider": "ttsProvider",
                "tts_voice_id": "aria",
                "voicemail_action": "hangup",
                "voicemail_message": "voicemailMessage",
                "voice_speed": 0.5,
            },
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.agents.with_raw_response.create(
            model="model",
            name="name",
            provider="openai",
            system_prompt="systemPrompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.agents.with_streaming_response.create(
            model="model",
            name="name",
            provider="openai",
            system_prompt="systemPrompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        agent = client.agents.retrieve(
            "agentId",
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.agents.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.agents.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        agent = client.agents.update(
            agent_id="agentId",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        agent = client.agents.update(
            agent_id="agentId",
            api_key="apiKey",
            context_window_messages=1,
            enabled=True,
            include_contact_metadata=True,
            max_tokens=1,
            model="model",
            name="name",
            provider="openai",
            system_prompt="systemPrompt",
            temperature=0,
            trigger_on_channels=["string"],
            trigger_on_message_types=["string"],
            voice={
                "enabled": True,
                "greeting": "Hi, thanks for calling Acme. How can I help you today?",
                "greetings": {"es": "Hola, soy Atlas. Preguntame lo que quieras."},
                "interruptible": True,
                "language": "en",
                "max_call_duration_minutes": 1,
                "max_idle_seconds": 5,
                "model": "openai/gpt-4o",
                "record_calls": True,
                "stt_model": "sttModel",
                "stt_provider": "sttProvider",
                "transfer_phone_number": "+14155551234",
                "tts_provider": "ttsProvider",
                "tts_voice_id": "aria",
                "voicemail_action": "hangup",
                "voicemail_message": "voicemailMessage",
                "voice_speed": 0.5,
            },
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.agents.with_raw_response.update(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.agents.with_streaming_response.update(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentUpdateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        agent = client.agents.list()
        assert_matches_type(SyncCursor[Agent], agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        agent = client.agents.list(
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(SyncCursor[Agent], agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(SyncCursor[Agent], agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(SyncCursor[Agent], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        agent = client.agents.delete(
            "agentId",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.agents.with_raw_response.delete(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.agents.with_streaming_response.delete(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_voices(self, client: Zavudev) -> None:
        agent = client.agents.list_voices()
        assert_matches_type(AgentListVoicesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_voices_with_all_params(self, client: Zavudev) -> None:
        agent = client.agents.list_voices(
            language="es",
        )
        assert_matches_type(AgentListVoicesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_voices(self, client: Zavudev) -> None:
        response = client.agents.with_raw_response.list_voices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListVoicesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_voices(self, client: Zavudev) -> None:
        with client.agents.with_streaming_response.list_voices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListVoicesResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: Zavudev) -> None:
        agent = client.agents.test(
            agent_id="agentId",
            message="Where is order ORD-12345?",
        )
        assert_matches_type(AgentTestResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_with_all_params(self, client: Zavudev) -> None:
        agent = client.agents.test(
            agent_id="agentId",
            message="Where is order ORD-12345?",
            execute_tools=True,
            history=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            use_knowledge_base=True,
        )
        assert_matches_type(AgentTestResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Zavudev) -> None:
        response = client.agents.with_raw_response.test(
            agent_id="agentId",
            message="Where is order ORD-12345?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentTestResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Zavudev) -> None:
        with client.agents.with_streaming_response.test(
            agent_id="agentId",
            message="Where is order ORD-12345?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentTestResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.test(
                agent_id="",
                message="Where is order ORD-12345?",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.create(
            model="model",
            name="name",
            provider="openai",
            system_prompt="systemPrompt",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.create(
            model="model",
            name="name",
            provider="openai",
            system_prompt="systemPrompt",
            context_window_messages=1,
            include_contact_metadata=True,
            max_tokens=1,
            temperature=0,
            trigger_on_channels=["string"],
            trigger_on_message_types=["string"],
            voice={
                "enabled": True,
                "greeting": "Hi, thanks for calling Acme. How can I help you today?",
                "greetings": {"es": "Hola, soy Atlas. Preguntame lo que quieras."},
                "interruptible": True,
                "language": "en",
                "max_call_duration_minutes": 1,
                "max_idle_seconds": 5,
                "model": "openai/gpt-4o",
                "record_calls": True,
                "stt_model": "sttModel",
                "stt_provider": "sttProvider",
                "transfer_phone_number": "+14155551234",
                "tts_provider": "ttsProvider",
                "tts_voice_id": "aria",
                "voicemail_action": "hangup",
                "voicemail_message": "voicemailMessage",
                "voice_speed": 0.5,
            },
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.agents.with_raw_response.create(
            model="model",
            name="name",
            provider="openai",
            system_prompt="systemPrompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.agents.with_streaming_response.create(
            model="model",
            name="name",
            provider="openai",
            system_prompt="systemPrompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.retrieve(
            "agentId",
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.update(
            agent_id="agentId",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.update(
            agent_id="agentId",
            api_key="apiKey",
            context_window_messages=1,
            enabled=True,
            include_contact_metadata=True,
            max_tokens=1,
            model="model",
            name="name",
            provider="openai",
            system_prompt="systemPrompt",
            temperature=0,
            trigger_on_channels=["string"],
            trigger_on_message_types=["string"],
            voice={
                "enabled": True,
                "greeting": "Hi, thanks for calling Acme. How can I help you today?",
                "greetings": {"es": "Hola, soy Atlas. Preguntame lo que quieras."},
                "interruptible": True,
                "language": "en",
                "max_call_duration_minutes": 1,
                "max_idle_seconds": 5,
                "model": "openai/gpt-4o",
                "record_calls": True,
                "stt_model": "sttModel",
                "stt_provider": "sttProvider",
                "transfer_phone_number": "+14155551234",
                "tts_provider": "ttsProvider",
                "tts_voice_id": "aria",
                "voicemail_action": "hangup",
                "voicemail_message": "voicemailMessage",
                "voice_speed": 0.5,
            },
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.agents.with_raw_response.update(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.agents.with_streaming_response.update(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentUpdateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.list()
        assert_matches_type(AsyncCursor[Agent], agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.list(
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(AsyncCursor[Agent], agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AsyncCursor[Agent], agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AsyncCursor[Agent], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.delete(
            "agentId",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.agents.with_raw_response.delete(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.agents.with_streaming_response.delete(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_voices(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.list_voices()
        assert_matches_type(AgentListVoicesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_voices_with_all_params(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.list_voices(
            language="es",
        )
        assert_matches_type(AgentListVoicesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_voices(self, async_client: AsyncZavudev) -> None:
        response = await async_client.agents.with_raw_response.list_voices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListVoicesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_voices(self, async_client: AsyncZavudev) -> None:
        async with async_client.agents.with_streaming_response.list_voices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListVoicesResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.test(
            agent_id="agentId",
            message="Where is order ORD-12345?",
        )
        assert_matches_type(AgentTestResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncZavudev) -> None:
        agent = await async_client.agents.test(
            agent_id="agentId",
            message="Where is order ORD-12345?",
            execute_tools=True,
            history=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            use_knowledge_base=True,
        )
        assert_matches_type(AgentTestResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncZavudev) -> None:
        response = await async_client.agents.with_raw_response.test(
            agent_id="agentId",
            message="Where is order ORD-12345?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentTestResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncZavudev) -> None:
        async with async_client.agents.with_streaming_response.test(
            agent_id="agentId",
            message="Where is order ORD-12345?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentTestResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.test(
                agent_id="",
                message="Where is order ORD-12345?",
            )
