import faust

app = faust.App(id="test",broker="kafka://localhost:9092",store="memory://")

# convenience func for launching the app
def main() -> None:
    app.main()

# Input topic, NOT managed by Faust. Marked
input_topic = app.topic('input', internal=False, partitions=1, value_type=str)

# Faust will create this topic for us.
colors_topic = app.topic('colors_topic', internal=True, partitions=1, value_type=str)

# Output, also NOT managed by Faust.
output_topic = app.topic('output', internal=False, partitions=1, value_type=str)

# Let's define a table to keep the count of valid RGB colors.
colors_count_table = app.Table('colors-count', key_type=str, value_type=int, partitions=1, default=int)

VALID_WORDS = ["red", "green", "blue"]

@app.agent(input_topic)
async def filter_colors(words):
    async for word in words:
        print(word)
        if word in VALID_WORDS:
            await colors_topic.send(value=word)

@app.agent(colors_topic)
async def colors_count(colors):
    async for color in colors:
        colors_count_table[color] += 1
        print(f'{color} has now been seen {colors_count_table[color]} times')
        await output_topic.send(value=colors_count_table[color])
