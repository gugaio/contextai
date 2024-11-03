class ToolExecutor:
    def execute_tools(tool_calls, current_agent):
        tool_messages = []
        for tool_call in tool_calls:
            result = current_agent.execute_tool(tool_call)
            if ToolExecutor._check_if_result_is_an_agent(result):
                current_agent = result
                result = f"Transfered to {current_agent.name}. Adopt persona immediately."
            tool_message = ToolExecutor._create_tool_message(tool_call.id, result)
            tool_messages.append(tool_message)
        return tool_messages, current_agent
    
    def _check_if_result_is_an_agent(result):
        return hasattr(result, 'task') and callable(getattr(result, 'execute_tool', None))
    
    def _create_tool_message(tool_call_id, result):
        return {
            "role": "tool",
            "tool_call_id": tool_call_id,
            "content": result
        }