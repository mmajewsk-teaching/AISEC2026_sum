import json
import os
import socket
import sys

import requests
from loguru import logger

DUMMY_TOKEN = "DUMMY_NOT_REGISTERED"


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()


def get_port_from_argv(default=8000):
    argv = sys.argv
    for i, arg in enumerate(argv):
        if arg == "--port" and i + 1 < len(argv):
            try:
                return int(argv[i + 1])
            except ValueError:
                pass
        if arg.startswith("--port="):
            try:
                return int(arg.split("=", 1)[1])
            except ValueError:
                pass
    env_port = os.getenv("PORT")
    if env_port:
        try:
            return int(env_port)
        except ValueError:
            pass
    return default


def write_dummy_tokens(token_path):
    with open(token_path, "w") as f:
        json.dump(
            {
                "player_auth_token": DUMMY_TOKEN,
                "player_game_public_token": DUMMY_TOKEN,
                "player_game_hidden_token": DUMMY_TOKEN,
            },
            f,
            indent=2,
        )


def print_registration_instructions(token_path):
    local_ip = get_local_ip()
    local_port = get_port_from_argv()
    log = logger.opt(colors=True)
    log.warning("<yellow>" + "=" * 70 + "</yellow>")
    log.warning("<yellow>You are NOT yet registered with the central game server.</yellow>")
    log.warning("")
    log.warning("<yellow>Step 1 — register your bot using THIS address:</yellow>")
    log.warning(f"    player_ip = <red><b>{local_ip}:{local_port}</b></red>")
    log.warning("")
    log.warning(f"<yellow>Step 2 — paste the returned tokens into <b>{token_path}</b>.</yellow>")
    log.warning("<yellow>Step 3 — restart this server.</yellow>")
    log.warning("<yellow>" + "=" * 70 + "</yellow>")


def has_dummy_tokens(token_path):
    try:
        with open(token_path) as f:
            tokens = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return True
    return any(tokens.get(k) == DUMMY_TOKEN for k in (
        "player_auth_token",
        "player_game_public_token",
        "player_game_hidden_token",
    ))


def bootstrap_tokens(token_path):
    if not os.path.exists(token_path):
        write_dummy_tokens(token_path)
    if has_dummy_tokens(token_path):
        print_registration_instructions(token_path)


def verify_public_token(token_path, server_url):
    if has_dummy_tokens(token_path):
        return False

    with open(token_path) as f:
        local = json.load(f)
    local_pub = local.get("player_game_public_token")

    try:
        r = requests.get(
            f"{server_url}/check_public_token",
            params={"public_token": local_pub},
            timeout=5,
        )
        valid = r.json().get("valid", False)
    except Exception as e:
        logger.error(f"Could not reach {server_url}/check_public_token: {e}")
        return False

    if not valid:
        logger.warning("Local public token not found on the central server.")
        print_registration_instructions(token_path)
        return False

    logger.info("Public token verified with central server")
    return True
