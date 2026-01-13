from google import genai
from google.genai import types
from call_function import available_functions, call_function
from prompts import system_prompt
from config import MODEL_NAME

def generate_content(client: genai.Client, messages: types.Content, verbose: bool) -> str:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            temperature=0,
        ),
    )
    
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")
    
    if verbose:
        if response.usage_metadata:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        else:
            raise RuntimeError("usage metadata is None")
        
    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)
                
    if not response.function_calls:
        return response.text
    
    function_response_list = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose=verbose)
        
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
            or not function_call_result.parts[0].function_response.response
        ):
            raise RuntimeError(f"Empty function response for {function_call.name}")
        
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
            
        function_response_list.append(function_call_result.parts[0])
            
        messages.append(types.Content(role="user", parts=function_response_list))