import inspect

type_map = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
    list: "array",
    dict: "object",
    type(None): "null",
}


def function_to_schema(func):
    """Convert function signature to pydantic schema."""
    try:
        signature = inspect.signature(func)
    except ValueError as e:
        raise ValueError(
            f"Failed to get signature for function {func.__name__}: {str(e)}"
        )
    
    parameters = {}
    required = []
    for param in signature.parameters.values():
        if param.default == param.empty:
            required.append(param.name)
        try:
            param_type = type_map.get(param.annotation, "string")
        except KeyError:
            raise ValueError(
                f"Unsupported type for parameter {param.name}: {param.annotation}"
            )
        parameters[param.name] = {"type": param_type}

    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": (func.__doc__ or "").strip(),
            "parameters": {
                "type": "object",
                "properties": parameters,
                "required": required,
            },
        },
    }

if __name__ == "__main__":
    def test_func(a: int, b: str, c: bool = True):
        """Test function for function_to_schema."""
        pass

    schema = function_to_schema(test_func)
    print(schema)