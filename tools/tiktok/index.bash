#!/bin/bash

# Script d'automatisation TikTok - Architecture optimale
# index.bash gère tout : boucle + stats + lance main.py puis publish.py

# Configuration
MAX_ITERATIONS=10
CURRENT_ITERATION=0
SUCCESSFUL=0
FAILED=0

# Fonction pour afficher l'heure
timestamp() {
    date +"%H:%M:%S"
}

# Fonction pour les logs
log_message() {
    echo "[$(timestamp)] $1"
}

# Fonction de countdown
countdown() {
    local seconds=$1
    local message=$2
    log_message "$message - $seconds seconds..."
    for ((i=seconds; i>=1; i--)); do
        printf "\r⏳ %d seconds remaining..." $i
        sleep 1
    done
    echo ""
}

# Fonction principale pour une itération
run_iteration() {
    CURRENT_ITERATION=$((CURRENT_ITERATION + 1))
    log_message "🔄 === ITERATION $CURRENT_ITERATION/$MAX_ITERATIONS ==="
    
    # ÉTAPE 1: Lancer main.py (actions de préparation)
    log_message "🎬 Step 1: Running preparation actions (main.py)..."
    echo "$(printf '=%.0s' {1..30})"
    
    python3 main.py
    main_exit_code=$?
    
    echo "$(printf '=%.0s' {1..30})"
    
    if [ $main_exit_code -ne 0 ]; then
        log_message "❌ main.py failed with exit code: $main_exit_code"
        FAILED=$((FAILED + 1))
        log_message "💔 Successful: $SUCCESSFUL, Failed: $FAILED"
        return 1
    fi
    
    log_message "✅ main.py completed successfully"
    
    # ÉTAPE 2: Lancer publish.py (création du post)
    log_message "📱 Step 2: Running post creation (publish.py)..."
    echo "📝 Real-time output from publish.py:"
    echo "$(printf '=%.0s' {1..50})"
    
    python3 publish.py
    publish_exit_code=$?
    
    echo "$(printf '=%.0s' {1..50})"
    
    if [ $publish_exit_code -eq 0 ]; then
        log_message "✅ publish.py executed successfully"
        SUCCESSFUL=$((SUCCESSFUL + 1))
        log_message "💚 Successful: $SUCCESSFUL, Failed: $FAILED"
        
        # ÉTAPE 3: Pause de 30s après succès
        if [ $CURRENT_ITERATION -lt $MAX_ITERATIONS ]; then
            countdown 30 "Post-success pause"
        fi
        
        return 0
    else
        log_message "❌ publish.py failed with exit code: $publish_exit_code"
        FAILED=$((FAILED + 1))
        log_message "💔 Successful: $SUCCESSFUL, Failed: $FAILED"
        
        # Pause plus longue en cas d'échec
        if [ $CURRENT_ITERATION -lt $MAX_ITERATIONS ]; then
            countdown 45 "Pause after failure"
        fi
        return 1
    fi
}

# Fonction principale
main() {
    echo "$(printf '=%.0s' {1..60})"
    echo "🤖 TIKTOK AUTOMATION SCRIPT - OPTIMAL VERSION"
    echo "$(printf '=%.0s' {1..60})"
    echo "Architecture:"
    echo "  • index.bash: Manages loop + stats + pauses"
    echo "  • main.py: Preparation actions only"
    echo "  • publish.py: Post creation with visible logs"
    echo ""
    echo "Each iteration:"
    echo "  1. Run main.py (prep: apps → close_all → tiktok_studio → create_grey)"
    echo "  2. Run publish.py (create post with real-time logs)"
    echo "  3. Pause 30s"
    echo "  4. Repeat"
    echo "$(printf '=%.0s' {1..60})"
    
    # Demander confirmation
    read -p "⚠️ Do you want to continue? (y/N): " response
    case $response in
        [yY]|[yY][eE][sS])
            ;;
        *)
            echo "❌ Operation cancelled by user"
            exit 0
            ;;
    esac
    
    # Demander le nombre d'itérations
    read -p "📊 Maximum number of iterations (default: 10): " max_iter
    if [[ $max_iter =~ ^[0-9]+$ ]] && [ $max_iter -gt 0 ]; then
        MAX_ITERATIONS=$max_iter
    else
        echo "Using default value: 10"
        MAX_ITERATIONS=10
    fi
    
    log_message "🚀 Starting automation loop (maximum: $MAX_ITERATIONS iterations)"
    log_message "⚠️ You have 5 seconds to switch to target window..."
    
    countdown 5 "Preparation"
    
    # Boucle principale
    while [ $CURRENT_ITERATION -lt $MAX_ITERATIONS ]; do
        if run_iteration; then
            # Succès - pause déjà gérée dans run_iteration
            if [ $CURRENT_ITERATION -lt $MAX_ITERATIONS ]; then
                countdown 15 "Pause between iterations"
            fi
        else
            # Échec - pause déjà gérée dans run_iteration
            :
        fi
    done
    
    # Résumé final
    log_message "🏁 === FINAL SUMMARY ==="
    log_message "Total iterations executed: $CURRENT_ITERATION"
    log_message "Successful iterations: $SUCCESSFUL"
    log_message "Failed iterations: $FAILED"
    
    if [ $CURRENT_ITERATION -gt 0 ]; then
        success_rate=$(( (SUCCESSFUL * 100) / CURRENT_ITERATION ))
        log_message "Success rate: ${success_rate}%"
    else
        log_message "Success rate: 0%"
    fi
    
    log_message "🎉 Automation completed!"
}

# Gestion des arguments
if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  -h, --help       Show this help message"
    echo "  --iterations N   Set maximum number of iterations"
    echo ""
    echo "Files required:"
    echo "  - main.py        (preparation actions)"
    echo "  - publish.py     (post creation)"
    exit 0
fi

if [ "$1" = "--iterations" ] && [ -n "$2" ]; then
    MAX_ITERATIONS=$2
fi

# Vérifications
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found in current directory"
    exit 1
fi

if [ ! -f "publish.py" ]; then
    echo "❌ Error: publish.py not found in current directory"
    exit 1
fi

# Lancer le script principal
main