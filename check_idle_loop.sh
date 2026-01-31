#!/bin/bash

export TK_SILENCE_DEPRECATION=1
export PATH="/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"

# base Python
PYTHON_BIN="/opt/anaconda3/bin/python"
PYTHON_SCRIPT="/Users/nkhyk664/Desktop/Time-circuit-screensaver/BTTF01.py"

# アイドル閾値（秒）
IDLE_THRESHOLD=60

while true; do
    # アイドル時間取得
    idle_time=$(ioreg -c IOHIDSystem | awk '/HIDIdleTime/ {print int($NF/1000000000); exit}')

    if [ "$idle_time" -ge "$IDLE_THRESHOLD" ]; then
        echo "✅ ${IDLE_THRESHOLD}秒アイドル状態なので Python 起動"
        "$PYTHON_BIN" "$PYTHON_SCRIPT"
        # 一度起動したら再度アイドルになるまで待つ
        while [ "$(ioreg -c IOHIDSystem | awk '/HIDIdleTime/ {print int($NF/1000000000); exit}')" -ge "$IDLE_THRESHOLD" ]; do
            sleep 1
        done
    fi
    sleep 1
done
