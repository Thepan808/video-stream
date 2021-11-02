# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""♦ **Bem vindo [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
👑 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Como você já sabe, eu sou um bot de tocar músicas na call e reproduzir vídeos!**

♦ **Descubra todos os comandos do Bot e como eles funcionam clicando no » 🧐 Botão comandos!**

♦️ **Para saber como usar este bot, clique no » ❓ Botão guia básico!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Adicione-me ao seu grupo ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Guia Básico", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("🧐 Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ Pae", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Grupo Oficial", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Canal Oficial", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "👑 Criador", url="https://t.me/xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Guia Básico para usar este bot:**

1.) **Primeiro, me adicione ao seu grupo.**
2.) **Então, promova-me como administrador e dê todas as permissões, exceto o Administrador Anônimo.**
3.) **Depois de me promover, digite /reload em grupo para atualizar os dados administrativos.**
3.) **Adicione @{ASSISTANT_NAME} ao seu grupo ou digite /userbotjoin para convidá-la.**
4.) **Ligue o bate-papo de vídeo primeiro antes de começar a reproduzir vídeo/música.**
5.) **Às vezes, recarregar o bot usando o comando /reload pode ajudá-lo a corrigir algum problema.**

📌 **Se o usuáriobot não se juntou ao bate-papo por vídeo, certifique-se se o chat de vídeo já está ligado ou digite /userbotleave e /userbotjoin e tente novamente.**

🧐 **Se você tiver uma pergunta de acompanhamento sobre este bot, você pode dizer no meu chat de suporte aqui: @{GROUP_SUPPORT}**

⚡ __Carregado pelo {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Para voltar", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🧐 **E ae fi de rapariga [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **pressione o botão abaixo para ler a explicação e ver a lista de comandos disponíveis !**

⚡ __Tururu ~ carregado por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Comandos de admin", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Comandos sudo", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("🧐 Comandos básicos", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Para voltar", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""♦️ aqui estão os comandos básicos:

» /play (Nome do som/link) - reproduzir música no bate-papo de vídeo
» /stream (nome/link) - transmitir a música ao vivo/rádio yt
» /vplay (video nome/ou marque/link) - reproduzir vídeo em bate-papo de vídeo
» /vstream - reproduzir vídeo ao vivo de yt live/m3u8
» /playlist - mostrar-lhe a lista de reprodução
» /video (Nome) - baixar vídeo do youtube
» /song (Nome) - baixar música do youtube
» /lyric (Nome) - pesquisar a letra da música
» /search (Nome) - pesquisar um link de vídeo youtube

» /ping - mostrar o status bot ping
» /uptime - mostrar o status de tempo de atividade do bot
» /alive - mostrar o bot informações vivas (em grupo)

⚡️ __Carregado pelo {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Para voltar", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""♦️ aqui estão os comandos administrativos:

» /pause - Pausar a música
» /resume - Resumir a música 
» /skip - Pular para próxima faixa do som
» /stop - Parar a transmissão 
» /vmute - Mutar o userbot no voice chat
» /vunmute - Desmutar o userbot no voice chat
» /reload - Atualizar o bot e atualiza a lista de admin
» /userbotjoin - Convidar o userbot para entrar ao grupo
» /userbotleave - ordenar que o userbot saia do grupo

⚡️ __Carregado pelo {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Para voltar", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""♦️ aqui é o sudo comandos:

» /rmw - limpar todos os arquivos rmw
» /rmd - limpar todos os arquivos baixados
» /leaveall - ordenar userbot para sair de todo o grupo

⚡ __Carregado pelo {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Para voltar", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("♦️ apenas administrador com gerenciamento de chats de voz permissão que pode tocar neste botão !", show_alert=True)
    await query.edit_message_text(
        f"⚙️ **Configurações do** {query.message.chat.title}\n\n⏸ : pause a música\n▶️ : resumir a música\n🔇 : mute o userbot\n🔊 : desmute o userbot\n⏹ : parar de tocar",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("⏹", callback_data="cbstop"),
                InlineKeyboardButton("⏸", callback_data="cbpause"),
                InlineKeyboardButton("▶️", callback_data="cbresume"),
            ],[
                InlineKeyboardButton("🔇", callback_data="cbmute"),
                InlineKeyboardButton("🔊", callback_data="cbunmute"),
            ],[
                InlineKeyboardButton("🗑 Fechar", callback_data="cls")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("♦️ apenas administrador com gerenciamento de chats de voz permissão que pode tocar neste botão !", show_alert=True)
    await query.message.delete()
