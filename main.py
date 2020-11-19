#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import logging

from telegram import (
    Update,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

logging.basicConfig(format="%(name)s - %(message)s", level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi!")


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Help!")


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main() -> None:
    try:
        token = sys.argv[1]
    except IndexError:
        try:
            with open("token.txt", "r") as token_file:
                token = token_file.read().strip("\n")
        except:
            logger.error("Add bot token to token.txt file before running!")
            sys.exit()

    updater = Updater(token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    logger.info("Ready to rock..!")
    updater.idle()


if __name__ == "__main__":
    main()
