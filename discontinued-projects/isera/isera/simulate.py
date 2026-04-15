from gfagraphs import Graph, Orientation
from Bio import SeqIO


def simulate_graph(
    backbone: str,
    parameters: dict,
) -> None:
    pass


def gfa_from_snp_file(
    input_sequence: str,
    snp_file: str,
    output_gfa: str
) -> None:
    """Pas un cas réaliste d'utilisation. Il va falloir manipuler des objets GFA tout du long
    Pour le moment on essaie, depuis une unique séquence, d'ajouter des SNP et d'en faire un GFA.
    On va utiliser notre librairie pour se simplifier la vie.
    """
    # We init empty graph
    sim_graph: Graph = Graph()

    # As we only simulate 2 genomes here, we iterate on sorted positions and break each time we notice a SNP.
    for record in SeqIO.parse(open(input_sequence), 'fasta'):
        name, sequence = record.id, record.seq

    sim_graph.add_path(
        identifier=name,
        chain=list(),
        name=name,
    )
    sim_graph.add_path(
        identifier='alt',
        chain=list(),
        name='alt',
    )

    current_node_name: int = 1
    previous_position: int = 0
    previous_nodes_to_connect: list | None = None
    with open(snp_file, 'r', encoding='utf-8') as snp_reader:
        next(snp_reader)
        for line in snp_reader:
            line_contents: list[str] = line.split('\t')
            start_position, ref_snp, alt_snp = int(
                line_contents[1]), line_contents[4], line_contents[9]
            # We add the node before the SNP
            sim_graph.add_node(
                name=(node_before := str(current_node_name)),
                sequence=sequence[previous_position:start_position-1]
            )
            # We create the edges between the previous nodes
            if previous_nodes_to_connect:
                for prev_node in previous_nodes_to_connect:
                    sim_graph.add_edge(
                        source=prev_node,
                        ori_source='+',
                        sink=node_before,
                        ori_sink='+',
                    )
            # We increase counter for future node name
            current_node_name += 1
            # We then add the two nodes of the SNP
            sim_graph.add_node(
                name=(node_ref := str(current_node_name)),
                sequence=ref_snp,
            )
            # We increase counter for future node name
            current_node_name += 1
            sim_graph.add_node(
                name=(node_alt := str(current_node_name)),
                sequence=alt_snp,
            )
            # We increase counter for future node name
            current_node_name += 1
            previous_nodes_to_connect = [node_ref, node_alt]
            previous_position = start_position
            for prev_node in previous_nodes_to_connect:
                sim_graph.add_edge(
                    source=node_before,
                    ori_source='+',
                    sink=prev_node,
                    ori_sink='+',
                )
            sim_graph.paths[name]['path'] += [
                (node_before, Orientation.FORWARD), (node_ref, Orientation.FORWARD)]
            sim_graph.paths['alt']['path'] += [
                (node_before, Orientation.FORWARD), (node_alt, Orientation.FORWARD)]

    # We add the remain as terminal node

    sim_graph.add_node(
        name=(node_before := str(current_node_name)),
        sequence=sequence[previous_position:]
    )
    # We create the edges between the previous nodes
    if previous_nodes_to_connect:
        for prev_node in previous_nodes_to_connect:
            sim_graph.add_edge(
                source=prev_node,
                ori_source='+',
                sink=node_before,
                ori_sink='+',
            )
    sim_graph.paths[name]['path'] += [(node_before, Orientation.FORWARD)]
    sim_graph.paths['alt']['path'] += [(node_before, Orientation.FORWARD)]

    sim_graph.save_graph(
        output_file=output_gfa,
        output_format='GFA1'
    )


gfa_from_snp_file(
    input_sequence='/home/sidubois/Workspace/isera/toy_examples/CASBIT01.fa',
    snp_file='/home/sidubois/Workspace/isera/toy_examples/snp_10_casbit01.refseq2simseq.map.txt',
    output_gfa='/home/sidubois/Workspace/isera/toy_examples/toy_gfa.gfa',
)
