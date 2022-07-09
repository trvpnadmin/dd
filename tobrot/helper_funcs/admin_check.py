#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52 | MaxxRider | 5MysterySD | Other Contributors 
#
# Copyright 2022 - TeamTele-LeechX
# 
# This is Part of < https://github.com/5MysterySD/Tele-LeechX >
# All Right Reserved

from pyrogram import enums

async def AdminCheck(client, chat_id, user_id):
    chat = await client.get_chat(chat_id)
    if chat.type == enums.ChatType.PRIVATE and chat_id in AUTH_CHANNEL:
        return True
    SELF = await client.get_chat_member(chat_id=chat_id, user_id=user_id)
    # https://git.colinshark.de/PyroBot/PyroBot/src/branch/master/pyrobot/modules/admin.py#L69
    if SELF.status != enums.ChatMemberStatus.ADMINISTRATOR or SELF.status != enums.ChatMemberStatus.OWNER:
        return False
    else:
        return True
