from olive.models import Task
from olive.parsers.v1.OliveListener import OliveListener
from olive.parsers.v1.OliveParser import OliveParser


class OliveListener(OliveListener):
    def __init__(self, tasks):
        self.tasks = tasks
        self.setup_current_task()

    def setup_current_task(self):
        self.current_task = {'tags': []}

    def exitDescription(self, ctx):
        text = ''
        for child in ctx.children:
            if hasattr(child, 'skip'):
                pass
            elif hasattr(child, 'text'):
                text += child.text
            else:
                text += child.getText()
        if isinstance(ctx.parentCtx, OliveParser.TaskContext) is False:
            ctx.text = text
        else:
            task = Task(
                description=text,
                tags=self.current_task.get('tags'),
                priority=self.current_task.get('priority'),
                size=self.current_task.get('size'),
            )
            self.tasks.append(task)
            self.setup_current_task()

    def enterLink(self, ctx):
        ctx.text = '<a href="%s">%s</a>' % (ctx.TEXT()[1], (ctx.TEXT()[0]))

    def enterPriority(self, ctx):
        ctx.skip = True

    def exitPriority(self, ctx):
        priority = ctx.getText().strip()
        self.current_task['priority'] = len(priority)

    def enterSize(self, ctx):
        ctx.skip = True

    def exitSize(self, ctx):
        self.current_task['size'] = ctx.getText().lower()[2:]

    def enterTag(self, ctx):
        ctx.skip = True

    def exitTag(self, ctx):
        self.current_task['tags'].append(ctx.getText().strip()[1:])

    def exitTasklist(self, ctx):
        return self.tasks
