#!/usr/bin/env python3
# 📜 ÁRBITRO DA VERDADE: VALIDADOR DE SOLUÇÃO INDEPENDENTE (v2)
# Projeto Ômega – Ferramenta de auditoria de código aberto.

import math
import sys
import re
import hashlib
import json
import argparse
from datetime import datetime

def parse_tsp_file(filepath):
    cidades = {}
    name = None
    with open(filepath, 'r') as f:
        node_coord_section = False
        for line in f:
            line = line.strip()
            if line.startswith("NAME"):
                name = line.split(":")[1].strip()
            if "NODE_COORD_SECTION" in line:
                node_coord_section = True
                continue
            if "EOF" in line:
                break
            if node_coord_section:
                parts = re.findall(r'[+-]?\d+(?:\.\d+)?', line)
                if len(parts) == 3:
                    node_id = parts[0]
                    x = float(parts[1])
                    y = float(parts[2])
                    cidades[node_id] = (x, y)
    return name, cidades

def read_solution_file(filepath):
    rota = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                rota.append(line)
    return rota

def calculate_total_distance(rota, cidades):
    distancia_total = 0
    for i in range(len(rota)):
        cidade_atual_id = rota[i]
        proxima_cidade_id = rota[(i + 1) % len(rota)]
        coord_atual = cidades[cidade_atual_id]
        coord_proxima = cidades[proxima_cidade_id]
        distancia = math.sqrt((coord_atual[0] - coord_proxima[0])**2 +
                              (coord_atual[1] - coord_proxima[1])**2)
        distancia_total += distancia
    return distancia_total

def validate_solution(rota, cidades):
    if len(rota) != len(cidades):
        return False, f"A rota tem {len(rota)} passos, mas o problema tem {len(cidades)} cidades."
    if len(set(rota)) != len(cidades):
        return False, "A rota contém cidades duplicadas ou omitiu cidades."
    if not all(cid in cidades for cid in rota):
        return False, "A rota contém cidades que não existem no arquivo .tsp."
    return True, "A rota é um caminho hamiltoniano válido."

def gerar_checksum(rota):
    return hashlib.sha256("".join(rota).encode()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description="Árbitro da Verdade - Validador de Solução para TSP")
    parser.add_argument("tsp", help="Arquivo .tsp do benchmark")
    parser.add_argument("rota", help="Arquivo .txt contendo a rota")
    parser.add_argument("--precision", type=int, default=2, help="Número de casas decimais para a distância")
    parser.add_argument("--json", action="store_true", help="Saída em formato JSON")
    parser.add_argument("--quiet", action="store_true", help="Modo silencioso (apenas resultado final)")
    args = parser.parse_args()

    tsp_name, cidades = parse_tsp_file(args.tsp)
    rota = read_solution_file(args.rota)
    valida, msg = validate_solution(rota, cidades)

    resultado = {
        "benchmark": tsp_name,
        "total_cidades": len(cidades),
        "tamanho_rota": len(rota),
        "valido": valida,
        "mensagem": msg,
        "distancia": None,
        "checksum": None,
        "data": datetime.now().isoformat()
    }

    if valida:
        distancia = calculate_total_distance(rota, cidades)
        resultado["distancia"] = round(distancia, args.precision)
        resultado["checksum"] = gerar_checksum(rota)

    if args.json:
        print(json.dumps(resultado, indent=4, ensure_ascii=False))
    else:
        if not args.quiet:
            print(f"Benchmark: {resultado['benchmark']}")
            print(f"Total de cidades: {resultado['total_cidades']}")
            print(f"Tamanho da rota: {resultado['tamanho_rota']}")
            print(f"Validação: {'✅ Válida' if valida else '❌ Inválida'} - {msg}")
            if valida:
                print(f"Distância total: {resultado['distancia']}")
                print(f"Checksum: {resultado['checksum']}")

if __name__ == "__main__":
    main()
