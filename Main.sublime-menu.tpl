[
    {
        "id": "edit",
        "children":
        [
            {
                "id": "lerem-text",
                "caption": "Lorem Text",
                "children":
                [
                    {
                        "caption": "Insert Lorem Text",
                        "command": "lorem_text",
                        "args": {
                            "word_count": null,
                            "paragraph_count": null
                        }
                    },
                    {
                        "caption": "Insert 10 Words of Lorem Text",
                        "command": "lorem_text",
                        "args": {
                            "word_count": 10,
                            "paragraph_count": 1
                        }
                    },
                    {
                        "caption": "Insert 50 Words of Lorem Text",
                        "command": "lorem_text",
                        "args": {
                            "word_count": 50,
                            "paragraph_count": 1
                        }
                    },
                    {
                        "caption": "Insert One Paragraph of Lorem Text",
                        "command": "lorem_text",
                        "args": {
                            "word_count": 100,
                            "paragraph_count": 1
                        }
                    }
                ]
            }
        ]
    },
    {
        "id": "preferences",
        "children":
        [
            {
                "id": "package-settings",
                "caption": "Package Settings",
                "children":
                [
                    {
                        "caption": "LoremText",
                        "children":
                        [
                            {
                                "caption": "README",
                                "command": "open_file",
                                "args": {"file": "${packages}/${_plugin_folder_name_}/README.md"}
                            },
                            {
                                "caption": "-"
                            },
                            {
                                "caption": "Settings - Default",
                                "command": "open_file",
                                "args": {"file": "${packages}/${_plugin_folder_name_}/LoremText.sublime-settings"}
                                
                            },
                            {
                                "caption": "Settings - User",
                                "command": "open_file",
                                "args": {"file": "${packages}/User/LoremText.sublime-settings"}
                            },
                            {
                                "caption": "-"
                            },
                            {
                                "caption": "Key Bindings - Default",
                                "command": "open_file",
                                "args": {
                                    "file": "${packages}/${_plugin_folder_name_}/Default (OSX).sublime-keymap",
                                    "platform": "OSX"
                                }
                            },
                            {
                                "caption": "Key Bindings - Default",
                                "command": "open_file",
                                "args": {
                                    "file": "${packages}/${_plugin_folder_name_}/Default (Windows).sublime-keymap",
                                    "platform": "Windows"
                                }
                            },
                            {
                                "caption": "Key Bindings - Default",
                                "command": "open_file",
                                "args": {
                                    "file": "${packages}/${_plugin_folder_name_}/Default (Linux).sublime-keymap",
                                    "platform": "Linux"
                                }
                            },
                            {
                                "caption": "Key Bindings - User",
                                "command": "open_file",
                                "args": {
                                    "file": "${packages}/User/Default (OSX).sublime-keymap",
                                    "platform": "OSX"
                                }
                                
                            },
                            {
                                "caption": "Key Bindings - User",
                                "command": "open_file",
                                "args": {
                                    "file": "${packages}/User/Default (Windows).sublime-keymap",
                                    "platform": "Windows"
                                }
                                
                            },
                            {
                                "caption": "Key Bindings - User",
                                "command": "open_file",
                                "args": {
                                    "file": "${packages}/User/Default (Linux).sublime-keymap",
                                    "platform": "Linux"
                                }
                                
                            }
                            
                        ]
                    }
                ]
            }
        ]
    }
]
