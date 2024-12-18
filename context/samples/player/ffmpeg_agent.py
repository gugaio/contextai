
from context.agents import Agent

class FFMpegAgent(Agent):

    ID = "ffmpeg_agent"
    NAME = "FFMpeg Agent"
    TASK = "use ffmpeg or ffprobe to extract video data"

    def __init__(self):
        super().__init__(id=self.ID, name=self.NAME, task=self.TASK)

    def instructions(self):
        if not "video" in self.context:
            return self._instruction_to_load_video()
        return self._instruction_to_extract_video_data_already_in_context()
    
    def _instruction_to_load_video(self):
        return "Video was not loaded yet. Call load_video_to_context tool to load the video, you need to provide the video ID and the player type."
        
    def _instruction_to_extract_video_data_already_in_context(self):
        return (
            "You are a ffmpeg agent and you can extract video data using ffmpeg."
            "Always answer in a sentence or less."
            "1. First you need to know the kind of video URL. User must choose between 'main' or 'single_audio'."
            "2. If user have not provided the kind, ask for it."
            "You must to know what type of data the user is interested in."
            f"The available fields are {self._ffmpeg_fields()}"
            "Then, call the extract video data tool with the fields that the user is interested in."
            "Provide the extracted video data to the user in a sentence."
        )

    def tools(self):
        if not "video" in self.context:
            return [self.load_video_to_context]
        else:
            return [self.extract_video_data]
    
    def load_video_to_context(self, video_id, player_type):
        """Load video to context tool."""
        self.context["video"] = {
            "id": video_id,
            "player": player_type
        }
        return "Video loaded successfully"

    def extract_video_data(self, kind):
        """Extract video data tool."""
        return (
            f"kind: {kind},"
            "bit_rate: '1000',"
            "channels: '2',"
            "duration: '50 seconds',"
            "format_name: 'mp4',"
            "frame_rate: '30',"
            "height: '1080',"
            "width: '1920'"
        )
    
    def _ffmpeg_fields(self):
        return "bit_rate, channels, duration, format_name, frame_rate, height, width"