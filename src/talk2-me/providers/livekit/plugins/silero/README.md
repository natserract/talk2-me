```bash
Version: livekit-plugins-silero = "=0.2.0"

Issue:
- Plugin.__init__() missing 1 required positional argument: 'package'
- Upgrade to 0.5.0: Updating onnxruntime (1.16.3 -> 1.17.3): Failed. Unable to find installation candidates for onnxruntime (1.17.3)

Solution:
> (solved in latest version, but idk can't install the latest version)

So, Duplicated the origin file and fix the issue:
 def __init__(self):
        super().__init__(__name__, __version__, __package__)
```

## References: 
- Custom plugin: https://docs.livekit.io/agents/plugins/#Building-your-own
- Latest commit: https://github.com/livekit/agents/commit/596ac9042b3ecbe40c270d035d5da8f25474e569