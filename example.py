"""
Streamlit Reasoning Visualizer - Example Application

This example demonstrates the component's capabilities without
requiring external dependencies like Ollama.

Run with: streamlit run example.py
"""

import streamlit as st
from reasoning_visualizer import visualizer, __version__

st.set_page_config(
    page_title="Reasoning Visualizer Demo",
    layout="wide",
    page_icon="🧠"
)

# Custom CSS for a cleaner look
st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc;
    }
    h1 {
        font-family: 'Inter', sans-serif;
        color: #0f172a;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Reasoning Visualizer Demo")
st.caption(f"Version {__version__} • Beautiful visualization for LLM reasoning processes")

st.markdown("---")

# Example 1: Standard <think> tags
st.subheader("Example 1: Standard `<think>` Tags")
st.markdown("Most common format used by models like DeepSeek-R1, Phi-4, etc.")

example1 = """<think>
Let me work through this step by step.

**Step 1: Understanding the problem**
We need to find the derivative of f(x) = x³ + 2x² - 5x + 3

**Step 2: Apply the power rule**
- d/dx(x³) = 3x²
- d/dx(2x²) = 4x
- d/dx(-5x) = -5
- d/dx(3) = 0

**Step 3: Combine the results**
f'(x) = 3x² + 4x - 5
</think>

The derivative of **f(x) = x³ + 2x² - 5x + 3** is:

$$f'(x) = 3x^2 + 4x - 5$$

This can be verified by applying the power rule to each term individually.
"""

visualizer(text=example1, key="example1")

st.markdown("---")

# Example 2: With boxed answer
st.subheader("Example 2: Mathematical Problem with LaTeX")
st.markdown("The component automatically renders `\\boxed{}` expressions.")

example2 = """<think>
I need to solve the quadratic equation x² - 5x + 6 = 0

Using the quadratic formula:
$$x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$$

Where a=1, b=-5, c=6:
- b² - 4ac = 25 - 24 = 1
- √1 = 1
- x = (5 ± 1) / 2

So x = 3 or x = 2

Let me verify:
- (3)² - 5(3) + 6 = 9 - 15 + 6 = 0 ✓
- (2)² - 5(2) + 6 = 4 - 10 + 6 = 0 ✓
</think>

The solutions to the equation **x² - 5x + 6 = 0** are:

\\boxed{x = 2 \\text{ or } x = 3}
"""

visualizer(text=example2, key="example2")

st.markdown("---")

# Example 3: No reasoning tags (just answer)
st.subheader("Example 3: Plain Response (No Tags)")
st.markdown("When no reasoning tags are found, the entire text is displayed as the answer.")

example3 = """Here's a quick overview of Python list comprehensions:

**Syntax:**
```python
[expression for item in iterable if condition]
```

**Examples:**
```python
# Square numbers
squares = [x**2 for x in range(10)]

# Filter even numbers
evens = [x for x in range(20) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
```

List comprehensions are more readable and often faster than equivalent `for` loops.
"""

visualizer(text=example3, key="example3")

st.markdown("---")

# Example 4: Alternative tag format
st.subheader("Example 4: Alternative `[THOUGHT]` Format")
st.markdown("Some models use bracket-style tags for reasoning.")

example4 = """[THOUGHT]
This is an interesting logic puzzle. Let me analyze it:

Given:
- All cats are mammals
- Some mammals are pets
- Fluffy is a cat

From "Fluffy is a cat" and "All cats are mammals":
→ Fluffy is a mammal (by syllogism)

However, "Some mammals are pets" doesn't guarantee that ALL mammals are pets.
So we cannot definitively conclude whether Fluffy is a pet.
[/THOUGHT]

Based on the given statements, we can conclude that **Fluffy is definitely a mammal**, but we **cannot determine** whether Fluffy is a pet. The statement "Some mammals are pets" doesn't imply that all mammals (including Fluffy) are pets.
"""

visualizer(text=example4, key="example4")

st.markdown("---")

st.info("💡 **Tip:** Click on the 'Reasoning Process' header to expand/collapse the thought section!")
