import pprint

from django.shortcuts import get_object_or_404, HttpResponse
from ..models import TemplateModel
from ..models import AvailableNextStatusModel
import networkx as nx
import matplotlib.pyplot as plt
from mplfonts.bin.cli import init
init()
import io



class Help():

    def __init__(self, template):
        self.row_height = 40
        self.col_width = 40
        self.edge_length = dict()
        self.template = template
        self.graph, sub_longest_path, length, y_offset = self.config_graph_by_template(self.template, 0, 0)

    def config_graph_by_template(self, template: TemplateModel, start_x, start_y):
        graph = nx.DiGraph()
        graph.add_nodes_from(template.statusmodel_set.all())
        total_width = 0
        total_height = 0
        all_sub_graphs = []
        for edge in AvailableNextStatusModel.objects.filter(src__template=template):
            graph.add_edge(
                edge.src, edge.dst
            )
            max_length = self.col_width
            height = self.row_height
            row = 0
            for row, sub_strategy in enumerate(edge.changestatusstrategymodel_set.all(), start=1):
                sub_graph, sub_longest_path, length, y_offset = self.config_graph_by_template(
                    sub_strategy.sub_template,
                    start_x,
                    start_y + height * (row + 1)
                )
                first, *_, last = sub_longest_path
                graph.add_edge(edge.src, first)
                graph.add_edge(last, edge.dst)
                all_sub_graphs.append(sub_graph)
                max_length = max(max_length, length)
            self.edge_length[(edge.src.id, edge.src.id)] = (max_length, row * height + height)
        longest_path = []
        for end_status in template.statusmodel_set.all():
            if p := nx.shortest_path(graph, template.start_status, end_status):
                if len(p) > len(longest_path):
                    longest_path = p

        for sub_graph in all_sub_graphs:
            graph = nx.compose(graph, sub_graph)

        return graph, longest_path, total_width, total_height

    def generate_fp(self):
        nx.draw_networkx(
            self.graph,
            # pos=pos,
            with_labels=True,
            node_size=1500,
            node_shape="s",
            alpha=0.5,
            linewidths=40
        )
        buffer = io.BytesIO()
        plt.savefig(buffer)
        plt.close()
        buffer.seek(0)
        return buffer

def status_grpah(request, template_id):
    obj = get_object_or_404(TemplateModel, pk=template_id)

    plt.figure(figsize=(20, 20))

    buffer = Help(obj).generate_fp()

    return HttpResponse(buffer.read(), content_type="image/png")