Output demo.gif
Set Shell "bash"
Set FontSize 18
Set Width 1200
Set Height 650
Set Theme "Dracula"
Set TypingSpeed 40ms
Set Padding 20

Type "source .venv/bin/activate"
Enter
Sleep 500ms
Type "clear"
Enter
Sleep 300ms

Type "# A blank report should NOT validate"
Enter
Sleep 400ms
Type "trg-validate trg/trg_report_template.yaml"
Enter
Sleep 2500ms

Type "clear"
Enter
Type "# A real system, benchmarked by tau-Voice, should"
Enter
Sleep 400ms
Type "trg-validate trg/trg_example_openai_realtime.yaml"
Enter
Sleep 2500ms

Type "clear"
Enter
Type "# Build the leaderboard across every baseline system"
Enter
Sleep 400ms
Type "trg-leaderboard > /dev/null && cut -d',' -f2,7,8 corpus/leaderboard.csv | column -s',' -t"
Enter
Sleep 4000ms
