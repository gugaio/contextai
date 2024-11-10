
from context.agents import Agent

class PlaybackAPIAnalystAgent(Agent):

    ID = "playback_api_analyst_agent"
    NAME = "Playback API Analyst Agent"
    TASK = "This Agent allows you analyse video data from playback api."

    def __init__(self):
        super().__init__(id=self.ID, name=self.NAME, task=self.TASK)

    def instructions(self):
        if not "video" in self.context:
            return self._instruction_to_load_video_to_context_tool()
        return self._instruction_to_extract_video_data_already_in_context()
    
    def _instruction_to_load_video_to_context_tool(self):
        return "Video was not loaded yet. Call load_video_to_context tool to load the video, you need to provide the video ID and the player type."
    
    def _instruction_to_extract_video_data_already_in_context(self):
        metadata_fields = self._metadata_fields()
        return (
            "The video is already loaded in the context, now we can extract the video data to reply any question about it."
            "1. But first you need to know the kind of video URL. User must choose between 'main' or 'single_audio'."
            "2. If user have not provided the kind, ask for it."
            "You must to know what type of data the user is interested in."
            f"The available fields are {self._metadata_fields()}"
            "Then, call the resume_playback_api_tool with the fields that the user is interested in."
            "Provide the resume video data to the user in a sentence."
        )

    def tools(self):
        if not "video" in self.context:
            return [self.load_video_to_context_tool]
        else:
            return [self.resume_playback_api_tool]
    
    def load_video_to_context_tool(self, video_id, player_type):
        """ Load video to context tool """
        self.context["video"] = {
            "id": video_id,
            "player": player_type
        }
        return "Video loaded successfully"
    
    def resume_playback_api_tool(self, fields):
        """ Resume playback api tool """
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