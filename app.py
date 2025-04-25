from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Contenu de l'article à afficher dans le blog
    blog_post = {
        'title': 'Mutable, Immutable... everything is object!',
        'image': 'img/python_logo.png',  # Image à afficher en haut
        'content': """
        <h2>Introduction</h2>
        <p>When diving into Python, you quickly learn one truth: <em>everything is an object</em>. 
        But what does that actually mean? This project helped me clarify a fundamental part of Python — 
        understanding mutable and immutable objects, how they behave differently, and why this distinction really matters. 
        By exploring identity, mutability, and function behavior, I gained a better grasp of how Python works under the hood, 
        and I’m excited to share what I learned.</p>
        
        <h2>ID and Type</h2>
        <p>Each object in Python has a unique identity, accessible through the <code>id()</code> function, and a defined <code>type()</code>. 
        Even if two variables have the same value, they might not reference the same object — unless Python decides to optimize memory using <em>interning</em>. 
        For instance:</p>
        <pre><code> 
a = 5
b = 5
print(id(a) == id(b))  # True (integers are interned)
        </code></pre>
        
        <p>However:</p>
        <pre><code>
x = [1, 2, 3]
y = [1, 2, 3]
print(id(x) == id(y))  # False (two different list objects)
        </code></pre>
        
        <h2>Mutable Objects</h2>
        <p>Mutable objects can be changed after they’re created. Lists, dictionaries, sets, and custom classes are common examples. 
        When you modify a mutable object, you're not creating a new one — you're changing the existing object.</p>
        <pre><code>
nums = [1, 2, 3]
print(id(nums))  # e.g. 139980728690048
nums.append(4)
print(id(nums))  # same id — object modified in place
        </code></pre>
        
        <h2>Immutable Objects</h2>
        <p>Immutable objects cannot be changed after they’re created. Common examples include integers, floats, strings, and tuples. 
        Any operation that <em>modifies</em> an immutable object actually creates a new one:</p>
        <pre><code>
name = "Alice"
print(id(name))  # e.g. 140122617347760
name += " Smith"
print(id(name))  # new id — new string object
        </code></pre>
        
        <h2>Why It Matters</h2>
        <p>Why should you care about this? Because Python treats mutable and immutable objects very differently when it comes to assignment, 
        copying, and function arguments. Mutables can lead to bugs if you're modifying shared data unintentionally, 
        while immutables are safer in concurrent code. Understanding this distinction is key to writing clean, predictable Python.</p>
        
        <h2>Function Argument Behavior</h2>
        <p>In Python, function arguments are passed by <em>object reference</em>. But this doesn't mean pass-by-reference in the traditional sense. 
        If the object is mutable, a function can change it in place. If it's immutable, the function can’t change the original — only work with a copy.</p>
        <pre><code>
def modify_list(lst):
    lst.append(100)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 100] — modified!

def modify_string(s):
    s += " World"

msg = "Hello"
modify_string(msg)
print(msg)  # "Hello" — unchanged
        </code></pre>
        
        <h2>What I Learned from Advanced Tasks</h2>
        <p>In advanced tasks, I experimented with copying and deep copying (<code>copy</code> vs <code>deepcopy</code>), 
        and the difference between shallow and deep equality. I also learned how to write my own classes that respect immutability principles, 
        using <code>@property</code> decorators and <code>__slots__</code> to control attributes.</p>
        <p>I also explored <em>interning</em> with small integers and strings, and how Python optimizes memory by reusing certain immutable objects. 
        These behind-the-scenes tricks make Python both efficient and sometimes surprising.</p>
        """
    }

    return render_template('index.html', post=blog_post)

if __name__ == '__main__':
    app.run(debug=True)
