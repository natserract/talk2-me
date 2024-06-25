from livekit.agents import WorkerOptions, cli

from .workflow import WorkflowManager


def run():
    workflow = WorkflowManager()
    cli.run_app(WorkerOptions(workflow.request_fnc))
