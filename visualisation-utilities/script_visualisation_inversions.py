from os import system, mkdir, path


def view_inversion(tool: str, param_set: dict):
    """
    Processes and visualizes genomic inversions using specified tools and parameters.

    Args:
        tool (str): The name of the tool to be used for visualization.
        param_set (dict): A dictionary containing the following keys:
            - "reference" (str): The reference path name.
            - "graph" (str): The graph file path.
            - "repo" (str): The directory path where output files will be stored.

    Raises:
        KeyError: If any of the required keys are missing in param_set.
        FileNotFoundError: If the input file "simulated_inv.bed" does not exist.

    """
    reference_path_name: str = param_set["reference"]
    graph: str = param_set["graph"]
    rep: str = param_set["repo"]
    fmt: str = param_set["format"]
    if not path.exists(rep):
        mkdir(rep)

    if fmt == "gfa1.1":
        name: str = graph[:-8] + '_gfa1.gfa'
        system(f"vg convert {graph[:-8]}.gfa -W -f > {name}")
    else:
        name: str = graph[:-8] + '.gfa'

    # odgi representation construction
    system(f"odgi build -g {name} -O -o {graph}")

    with open("simulated_inv.bed", 'r') as bedreader:
        for line in bedreader:
            scaff, posx, posy, invcode, ilen = line.split('\t')
            if invcode in selected_inversions:
                # --context-steps {x}
                system(
                    f"odgi extract -i {graph} -o {rep}/{invcode}.og --path-range {reference_path_name}:{max(0,int(posx)-safe_context)}-{min(int(posy)+safe_context,float('inf'))}"
                )
                system(
                    f"odgi view -g -i {rep}/{invcode}.og > {rep}/{invcode}.gfa"
                )
                system(
                    f"pancat grapher {rep}/{invcode}.gfa {rep}/{invcode}.html{' -f' if fmt == 'rgfa' else ''}"
                )


selected_inversions: list[str] = [
    "INV18", "INV61", "INV62", "INV91", "INV100"
]
x: int = 3  # nombres de noeuds à extraire de chaque côté de l'inversion
safe_context: int = 1000  # combien de bases à droite et gauche de l'inversion

params: dict = {
    "pggb": {
        "reference": "scaffold_6",
        "graph": "pggb_div00_opti.og",
        "repo": "visu_pggb",
        "format": "gfa1.0",
    },
    "mgc": {
        "reference": "CARC#0#scaffold_6",
        "graph": "mgc_div00_opti.og",
        "repo": "visu_mgc",
        "format": "gfa1.1",
    },
    "mg": {
        "reference": "scaffold_6",
        "graph": "mg_div00_opti.og",
        "repo": "visu_mg",
        "format": "rgfa",
    }
}

for tool, param_set in params.items():
    view_inversion(tool, param_set)
