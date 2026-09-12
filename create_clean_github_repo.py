#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour créer un nouveau repository GitHub propre
Auteur: Dady Akrou Cyrille
Date: 2025
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, cwd=None):
    """Exécute une commande et retourne le résultat"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd,
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip(), True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'exécution de: {command}")
        print(f"Code d'erreur: {e.returncode}")
        print(f"Sortie d'erreur: {e.stderr}")
        return e.stderr.strip(), False

def main():
    """Fonction principale"""
    print("🚀 Création d'un repository GitHub propre pour le projet Chest X-Ray")
    print("=" * 70)
    
    # Vérifier que nous sommes dans le bon répertoire
    current_dir = Path.cwd()
    print(f"📁 Répertoire actuel: {current_dir}")
    
    # Instructions pour l'utilisateur
    print("\n📋 INSTRUCTIONS:")
    print("1. Allez sur https://github.com/new")
    print("2. Créez un nouveau repository avec le nom: 'chest-xray-pneumonia-detection-clean'")
    print("3. Description suggérée: 'Système de détection automatique de pneumonie sur radiographies thoraciques - Projet ML complet'")
    print("4. Laissez-le PUBLIC")
    print("5. NE PAS initialiser avec README, .gitignore ou licence (nous avons déjà tout)")
    print("6. Cliquez sur 'Create repository'")
    
    input("\n⏸️  Appuyez sur Entrée une fois que vous avez créé le repository...")
    
    # Vérifier le statut Git
    print("\n🔍 Vérification du statut Git...")
    status, success = run_command("git status --porcelain")
    if success:
        if status:
            print(f"⚠️  Fichiers non commitées détectés:")
            print(status)
        else:
            print("✅ Tous les fichiers sont commitées")
    
    # Vérifier les remotes
    print("\n🔗 Vérification des remotes...")
    remotes, success = run_command("git remote -v")
    if success:
        print(f"Remotes actuels:\n{remotes}")
    
    # Pousser vers le nouveau repository
    print("\n📤 Push vers le nouveau repository GitHub...")
    push_output, success = run_command("git push -u origin master")
    
    if success:
        print("✅ Push réussi!")
        print(f"Sortie: {push_output}")
        print("\n🎉 Votre projet propre est maintenant sur GitHub!")
        print("🔗 URL: https://github.com/CyrilleAD/chest-xray-pneumonia-detection-clean")
        
        # Afficher un résumé des fichiers trackés
        print("\n📋 Fichiers trackés dans le repository:")
        files, success = run_command("git ls-files")
        if success:
            for file in files.split('\n'):
                if file.strip():
                    print(f"  ✓ {file}")
                    
    else:
        print("❌ Échec du push")
        print(f"Erreur: {push_output}")
        print("\n🔧 Solutions possibles:")
        print("1. Vérifiez que le repository GitHub a été créé")
        print("2. Vérifiez vos permissions GitHub")
        print("3. Essayez de pousser manuellement: git push -u origin master")
    
    print("\n" + "=" * 70)
    print("✨ Script terminé")

if __name__ == "__main__":
    main()