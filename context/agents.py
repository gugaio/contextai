
from base_agent import Agent
from tools import execute_ffmpeg, look_up_playback_api


ffmpeg_agent = Agent(
    name="Player FFmpeg Analyst Agent",
    instructions=(
        "You are ffmpeg analyst agent."
        "Always answer in a sentence or less."
        "5. If the task if get information with ffmpeg, call execute ffmpeg tool."
    ),
    tools=[execute_ffmpeg],
)

def transfer_to_ffmpeg_agent(video_id, player_type):
    """Transfer to ffmpeg agent."""
    return ffmpeg_agent

triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You are a triage agent."
        "You goal is to help users execute the right agent or tool."
        "Always answer in a sentence or less."
        "Follow the following routine with the user:"
        "1. First, you need to know the video ID and player type. Ask users to provide both.\n"
        " - unless the user has already provided these two information.\n"
        "2. Then ask if user can analyse video metadata from playback api or extract information with ffmpeg.\n"
        "3. ONLY accept the two options, or ask user again.\n"
        "4. If the task is analyse data from playback api, call tool look up playback api info."
        "5. If the task if get information with ffmpeg, Transfer to Player FFmpeg Agent."
        ""
    ),
    tools=[look_up_playback_api, transfer_to_ffmpeg_agent],
)

def initial_agent():
    return triage_agent
