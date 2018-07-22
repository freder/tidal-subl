SESSION="tidal"
SAMPLES_DIR="~/Library/Application\ Support/SuperCollider/downloaded-quarks/Dirt-Samples/"

tmux -2 attach-session -t $SESSION || tmux -2 \
	new-session -s $SESSION \; \
	send-keys -t $SESSION "open ./superdirt.sc" C-m \; \
	send-keys -t $SESSION "open $SAMPLES_DIR" C-m \; \
	send-keys -t $SESSION "TIDAL_BOOT_PATH=$TIDAL_BOOT_PATH TIDAL_TEMPO_IP=$TIDAL_TEMPO_IP GHCI=$GHCI tidal" C-m \; \
	send-keys -t $SESSION ":script ./Tidal.ghci" C-m \;
