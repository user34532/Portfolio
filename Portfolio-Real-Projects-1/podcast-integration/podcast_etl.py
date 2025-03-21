import json

# Load podcast data
with open('podcast_data.json', 'r') as f:
    data = json.load(f)

# Extract episode titles
titles = [episode['title'] for episode in data['episodes']]

# Save titles
with open('episode_titles.txt', 'w') as f:
    f.writelines("\n".join(titles))

print("Podcast episode titles extracted successfully!")
