
from agents.base_agent import Agent

class PlaybackAPIAnalystAgent(Agent):

    ID = "playback_api_analyst_agent"
    NAME = "Playback API Analyst Agent"
    TASK = "analyse video data from playback api"

    def __init__(self):
        super().__init__(id=self.ID, name=self.NAME, task=self.TASK)

    def instructions(self):
        if not "video" in self.context:
            return "Call load video to the context tool"
        metadata_fields = self._metadata_fields()
        return (
            "You are playback api analyst agent."
            "Always answer in a sentence or less."
            "1. If users did not ask for a specific fields, tell them that video metadata is available in context window."
            "2. If users ask for a specific fields, call filter playback api tool."
            "You must provide the fields queried by user, based on the available fields."
            f"The available fields are {metadata_fields}"
            "Identify the video metadata fields that the user is interested in and provide to the tool fields param as a comma separated string."
            "When you get the filtered video metadata, provide the information to the user in a sentence."
        )

    def tools(self):
        if not "video" in self.context:
            return [self.load_video_to_context]
        else:
            return [self.filter_playback_api]
    
    def load_video_to_context(self, video_id, player_type):
        self.context["video"] = {
            "id": video_id,
            "player": player_type
        }
        return "Video loaded successfully"
    
    def filter_playback_api(self, fields):
        print("Summary:", fields)
        return (
            "title: 'Joao video',"
            "description: '10 years old bitrhday',"
            "keywords: 'video keywords',"
            "duration: '50 seconds',"
            "size: 'FullHD',"
            "format: 'Wide',"
            "resolution: '1920x980',"
            "codec: 'h264'"
        )

    def _metadata_fields(self):
        return "title, description, keywords, duration, size, format, resolution, codec"