curl --location --request POST 'https://api.openai.com/v1/engines/davinci-codex/completions' --header 'Content-Type: application/json' --header 'Authorization: Bearer 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' --data-raw "{
  'prompt': 'sebutkan 1 nama rendom',
  'temperature': 0.28,
  'max_tokens': 3406,
  'top_p': 1,
  'frequency_penalty': 0,
  'presence_penalty': 0
}"