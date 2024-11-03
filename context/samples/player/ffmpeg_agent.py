
from agents.base_agent import Agent

class FFMpegAgent(Agent):

    def __init__(self):
        id = "ffmpeg_agent"
        name = "FFMpeg Agent"
        task = "use video with ffmpeg"
        super().__init__(id=id,name=name, task=task)

    def instructions(self):
        if not "video" in self.context:
            return "Call load video to the context tool"
        
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