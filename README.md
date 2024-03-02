# Aoles RTC
Aim to make RTC easy.

Only support python 3.10.13 now.

A rtc library supporting janus & p2p, more program languages (python, C#, C++ now) in the future.

[AolesRTC github](https://github.com/laoleshisui/pyaolesrtc)

# Demo video
[BiliBili](https://www.bilibili.com/video/BV1ta4y127w8/?spm_id_from=333.337.search-card.all.click&vd_source=46ec781a0f61978d02e1d561b34fa772)

# How to install
## manually(recommended currently)
    python3.10 setup.py sdist build
    pip3.10 install ./dist/aolesrtc-xxx.tar.gz

## pypi
    pip3.10 install aolesrtc

# Dependences
## Linux(x86_64)
    export LD_LIBRARY_PATH=/path/to/aolesrtc/lib/linux/x86_64/lib
## Mac(arm)(recommended currently)
    brew install python@3.10

# Prepare raw files for test
```
#video
ffmpeg -i source.mp4 \
-f rawvideo -pix_fmt yuv420p -s 1080x1920 -r 25 \
-t 20 -y ./examples/video_1080x1920_25fps.yuv

#audio
ffmpeg -i source.mp4 \
-f  s16le -ac 1 -ar 24000 \
-t 20 -y ./examples/video_24000.pcm
```

# Examples
## P2P
See examples/p2pprocessor.py for more details

1. Create a sender to send video frame and audio sample. If the receiver's id is known, you can just connect it with the id and nothing else.
```python
def CreateSender():
    Controller.LoadConfigFile("./defaults.yaml")
    Controller.InitLog("./p2p_sender.log")

    time.sleep(3) # wait for receiver logined
    peer_data_1 = CreatePeer(is_sender=True, is_receiver=False)
    time.sleep(1)

    # assume the last id is of the sender
    receiver_id = last_id - 1
    print("ConnectToPeer (receiver_id = last_id - 1):", receiver_id)
    peer_data_1["p2p_client"].ConnectToPeer(receiver_id)

    send_yuv_thread = threading.Thread(target=send_yuv, args=(peer_data_1, "/path/to/video_1080x1920_25fps.yuv",))
    send_yuv_thread.start()

    send_pcm_thread = threading.Thread(target=send_pcm, args=(peer_data_1, "/path/to/video_24000_s16le.pcm",))
    send_pcm_thread.start()

    send_yuv_thread.join()
    send_pcm_thread.join()
```
2. Create a receiver to receive video frame and audio sample, you can get the data in the callback and also play audio automatically if not callback

```python
def CreateReceiver():
    Controller.LoadConfigFile("./defaults.yaml")
    Controller.InitLog("./p2p_receiver.log")

    peer_data_2 = CreatePeer(is_sender=False, is_receiver=True)

    render(peer_data_2["video_sink"])
```

## Janus
See examples/videoroom.py and examples/audiobridge.py for details

# Contact
QQ Group: 947652097