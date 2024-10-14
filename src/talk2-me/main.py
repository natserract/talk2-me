from livekit.agents import WorkerOptions, cli

from workflow import WorkflowManager

if __name__ == "__main__":
    workflow = WorkflowManager()
    cli.run_app(WorkerOptions(workflow.request_fnc))
