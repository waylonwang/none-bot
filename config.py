config = {
    'fallback_command': '',  # ''natural_language.process',
    'fallback_command_after_nl_processors': '',  # ''ai.tuling123',
    'command_start_flags': ('', '/', '／'),  # Add '' (empty string) here to allow commands without start flags
    'command_name_separators': ('->', '::', '/'),  # Regex
    'command_args_start_flags': ('，', '：', ',', ', ', ':', ': ', '[\\s]'),  # Regex
    'command_args_separators': ('，', ',', '[\\s]'),  # Regex

    'message_sources': [
        {
            'via': 'coolq_http_api',
            'login_id': '3546065794',
            'superuser_id': '216376',
            'api_url': 'http://127.0.0.1:5700',
            'token': 'LRqxVa7G3a9c'
        }
    ],

    'biz_server': [
        {
            'via': 'score_biz_server',
            'login_id': '3546065794',
            'api_url': 'http://127.0.0.1:5800',
            'api_key': 'jkvu0g44ey1h1jfd2x9gkym8pejs7228'
        }
    ]
}
