#!/bin/bash
# backdate_last5.sh  - make one commit for each of the last 5 days (incl. today)

FILE="history.txt"
touch "$FILE"

# Number of days back (4 days ago .. today => 5 days total)
for i in $(seq 4 -1 0); do
  DATE=$(date -I -d "$i days ago")
  echo "Backdated entry for $DATE" >> "$FILE"
  git add "$FILE"

  GIT_AUTHOR_DATE="$DATE 12:00:00" GIT_COMMITTER_DATE="$DATE 12:00:00" \
    git commit -m "Backdated commit for $DATE"
done

git push origin main
