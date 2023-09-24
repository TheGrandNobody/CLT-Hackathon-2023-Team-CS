import tiktoken

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
with open("input.txt", "r") as f:
    text = f.read()
ninput = len(encoding.encode(text))
input = 0.012 * ninput / 1000

with open("output.txt", "r") as f:
    text = f.read()
noutput = len(encoding.encode(text))
output = 0.016 * noutput / 1000

with open("train.txt", "r") as f:
    text = f.read()
ntraining = len(encoding.encode(text))
training = 10000 * 0.008 * ntraining / 1000

print("GPT-3.5-turbo")
y_io_costs = (input + output) * 16
yearly = y_io_costs
monthly = (y_io_costs / 12)
y_school = (y_io_costs * 64)
m_school = (y_io_costs * 64/12)
print("Training:", training, "USD")
print("Monthly price per teacher:", monthly, "USD","Yearly price per teacher:", yearly, "USD")
print("Monthly price per school: ", m_school, "USD", "Yearly price per school:", y_school, "USD")
print()
print()
y4_io_costs = ((input * 1.33 + output * 1.125) * 16)
yearly_4 = y4_io_costs
monthly_4 = (y4_io_costs / 12)
y4_school = (y4_io_costs * 64)
m4_school = (y4_io_costs * 64/12)
print("GPT-4")
print("Training:", training * 1.25, "USD")
print("Monthly price per teacher:", monthly_4, "USD","Yearly price per teacher:", yearly_4, "USD")
print("Monthly price per school: ", m4_school, "USD", "Yearly price per school:", y4_school, "USD")

