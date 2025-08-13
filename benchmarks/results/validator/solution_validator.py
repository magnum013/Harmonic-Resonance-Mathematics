#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
📜 ÁRBITRO DA VERDADE – VALIDADOR DE SOLUÇÃO INDEPENDENTE
Projeto Ômega – Módulo de Auditoria Aberta v1.0
======================================================================
Descrição:
    Ferramenta de validação para soluções do Problema do Caixeiro Viajante (TSP).
    Garante integridade, calcula distância e regista auditoria.

Autor:
    Luan Borges Fernandes – Projeto Ômega
======================================================================
"""

import math
import sys
import re
import os
import hashlib
from datetime import datetime

# Pasta de logs
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

def parse_tsp_file(filepath):
    """Lê arquivo .tsp e retorna {cidade_id: (x, y)}"""
    cidades = {}
    with open(filepath, 'r') as f:
        node_coord_section = False
        for line in f:
            line = line.strip()
            if "NODE_COORD_SECTION" in line:
                node_coord_section = True
                continue
            if "EOF" in line or line == "":
                break
            if node_coord_section:
                parts = re.findall(r'[+-]?\d+(?:\.\d+)?', line)
                if len(parts) >= 3:
                    node_id = parts[0]
                    x = float(parts[1])
                    y = float(parts[2])
                    cidades[node_id] = (x, y)
    print(f"🌍 Benchmark '{filepath}' lido: {len(cidades)} cidades.")
    return cidades

def read_solution_file(filepath):
    """Lê arquivo de rota e retorna lista de IDs."""
    rota = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                rota.append(line)
    print(f"🗺️  Rota '{filepath}' lida: {len(rota)} passos.")
    return rota

def calculate_total_distance(rota, cidades):
    """Calcula distância total da rota."""
    distancia_total = 0
    for i in range(len(rota)):
        cid_atual = rota[i]
        cid_prox = rota[(i + 1) % len(rota)]
        coord_atual = cidades[cid_atual]
        coord_prox = cidades[cid_prox]
        distancia_total += math.hypot(coord_atual[0] - coord_prox[0],
                                      coord_atual[1] - coord_prox[1])
    return distancia_total

def checksum_solution(rota):
    """Gera checksum SHA-256 da rota para auditoria."""
    rota_str = "-".join(rota)
    return hashlib.sha256(rota_str.encode()).hexdigest()

def validate_solution(rota, cidades):
    """Valida integridade da solução."""
    if len(rota) != len(cidades):
        return False, f"❌ Passos na rota ({len(rota)}) != cidades ({len(cidades)})"
    if len(set(rota)) != len(cidades):
        return False, "❌ Cidades duplicadas ou ausentes."
    return True, "✅ Caminho hamiltoniano válido."

def log_auditoria(tsp_file, sol_file, valido, distancia, checksum):
    """Registra auditoria no arquivo de log."""
    log_path = os.path.join(RESULTS_DIR, "auditoria_validacoes.txt")
    with open(log_path, "a") as log:
        log.write(f"[{datetime.now()}] Arquivo: {tsp_file} | Solução: {sol_file} | "
                  f"Validade: {valido} | Distância: {distancia:.2f} | Checksum: {checksum}\n")

def arbitro_da_verdade(tsp_file, sol_file):
    print("======================================================================")
    print("    📜 INICIANDO O ÁRBITRO DA VERDADE – Projeto Ômega v1.0")
    print("======================================================================")

    try:
        cidades = parse_tsp_file(tsp_file)
        rota = read_solution_file(sol_file)

        valido, msg = validate_solution(rota, cidades)
        print(msg)

        if valido:
            distancia = calculate_total_distance(rota, cidades)
            checksum = checksum_solution(rota)
            print(f"🏁 Distância Total: {distancia:.2f}")
            print(f"🔑 Checksum da Rota: {checksum[:16]}...")

            log_auditoria(tsp_file, sol_file, "Válida", distancia, checksum)
        else:
            log_auditoria(tsp_file, sol_file, "Inválida", 0, "N/A")
            print("⚠️ Validação falhou. Distância não calculada.")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

    print("\n📡 Assinatura: Projeto Ômega – Harmonic Resonance Mathematics")
    print("======================================================================")

if __name__ == "__main__":
    # Uso:
    # python solution_validator.py berlin52.tsp rota.txt
    if len(sys.argv) != 3:
        print("Uso: python solution_validator.py <arquivo.tsp> <solucao.txt>")
        sys.exit(1)
    arbitro_da_verdade(sys.argv[1], sys.argv[2])
