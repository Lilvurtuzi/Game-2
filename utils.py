import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import x
import streamlit as st
import random

def generate_function(level):
    """Generate a rational function based on difficulty level"""
    random.seed()  # Ensure randomness
    
    if level == "Easy":
        # Simple rational functions with linear factors
        num_coeff = random.randint(1, 3)
        num_root = random.randint(1, 5)
        den_root1 = random.randint(1, 5)
        den_root2 = random.randint(6, 10)
        
        # Ensure denominator roots are different from numerator
        while den_root1 == num_root:
            den_root1 = random.randint(1, 5)
        while den_root2 == num_root:
            den_root2 = random.randint(6, 10)
        
        num = num_coeff * (x - num_root)
        den = (x - den_root1) * (x + den_root2)
        
    elif level == "Medium":
        # Rational functions with quadratic factors
        num_roots = [random.randint(-3, 3), random.randint(-3, 3)]
        den_roots = [random.randint(-5, -1), random.randint(1, 5)]
        
        # Ensure some complexity
        num = (x - num_roots[0]) * (x - num_roots[1])
        den = (x - den_roots[0]) * (x - den_roots[1])
        
    else:  # Hard
        # Complex rational functions with holes
        common_factor = random.randint(1, 3)
        num_factor = random.randint(-4, 4)
        den_factor1 = random.randint(-3, 3)
        den_factor2 = random.randint(1, 5)
        
        # Ensure denominator factors are different
        while den_factor1 == den_factor2:
            den_factor1 = random.randint(-3, 3)
        
        # Create a function with a hole
        num = (x - common_factor) * (x - num_factor)
        den = (x - common_factor) * (x - den_factor1) * (x - den_factor2)
    
    return num / den

def get_features(expr):
    """Extract key features of a rational function"""
    try:
        expr = sp.simplify(expr)
        num, den = sp.fraction(expr)
        
        # Initialize features
        features = {
            "x_intercepts": [],
            "y_intercept": 0,
            "holes": [],
            "asymptotes": [],
            "end_behavior": None
        }
        
        # Find x-intercepts (where numerator = 0)
        try:
            x_intercepts = sp.solve(num, x)
            features["x_intercepts"] = [complex(xi).real for xi in x_intercepts if complex(xi).imag == 0]
        except:
            features["x_intercepts"] = []
        
        # Find y-intercept (substitute x = 0)
        try:
            y_int = expr.subs(x, 0)
            if y_int.is_real:
                features["y_intercept"] = float(y_int)
        except:
            features["y_intercept"] = 0
        
        # Find holes (common factors in numerator and denominator)
        try:
            original_num, original_den = sp.fraction(expr)
            common_factors = sp.gcd(original_num, original_den)
            
            if common_factors != 1:
                hole_x_vals = sp.solve(common_factors, x)
                for hole_x in hole_x_vals:
                    if hole_x.is_real:
                        # Calculate y-coordinate of hole
                        simplified_expr = sp.simplify(expr)
                        try:
                            hole_y = simplified_expr.subs(x, hole_x)
                            if hole_y.is_finite and hole_y.is_real:
                                features["holes"].append((float(hole_x), float(hole_y)))
                        except:
                            pass
        except:
            pass
        
        # Find vertical asymptotes (where denominator = 0 but not holes)
        try:
            den_roots = sp.solve(den, x)
            hole_x_vals = [hole[0] for hole in features["holes"]]
            
            for root in den_roots:
                if root.is_real and float(root) not in hole_x_vals:
                    features["asymptotes"].append(float(root))
        except:
            pass
        
        # Find end behavior
        try:
            end_behavior = sp.limit(expr, x, sp.oo)
            features["end_behavior"] = end_behavior
        except:
            features["end_behavior"] = None
        
        return features
        
    except Exception as e:
        st.error(f"Error analyzing function: {str(e)}")
        return {
            "x_intercepts": [],
            "y_intercept": 0,
            "holes": [],
            "asymptotes": [],
            "end_behavior": None
        }

def graph_function(expr):
    """Create a graph of the rational function with proper styling"""
    try:
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Set up the plot with a dark theme
        fig.patch.set_facecolor('#0E1117')
        ax.set_facecolor('#262730')
        
        # Create function for plotting
        f = sp.lambdify(x, expr, modules=["numpy"])
        
        # Create x values, avoiding asymptotes
        features = get_features(expr)
        asymptotes = features["asymptotes"]
        
        # Split domain around asymptotes
        x_ranges = []
        all_points = [-10] + sorted(asymptotes) + [10]
        
        for i in range(len(all_points) - 1):
            start = all_points[i]
            end = all_points[i + 1]
            
            if i == 0:
                x_range = np.linspace(start, end - 0.1, 200)
            elif i == len(all_points) - 2:
                x_range = np.linspace(start + 0.1, end, 200)
            else:
                x_range = np.linspace(start + 0.1, end - 0.1, 200)
            
            x_ranges.append(x_range)
        
        # Plot function in each range
        for x_range in x_ranges:
            y_vals = []
            x_vals = []
            
            for xi in x_range:
                try:
                    yi = f(xi)
                    if np.isfinite(yi) and abs(yi) < 50:  # Limit y-range for better visualization
                        y_vals.append(yi)
                        x_vals.append(xi)
                    else:
                        if y_vals:  # Plot accumulated points
                            ax.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)' if len(ax.lines) == 0 else "")
                        y_vals = []
                        x_vals = []
                except:
                    if y_vals:  # Plot accumulated points
                        ax.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)' if len(ax.lines) == 0 else "")
                    y_vals = []
                    x_vals = []
            
            # Plot remaining points
            if y_vals:
                ax.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)' if len(ax.lines) == 0 else "")
        
        # Add vertical asymptotes
        for asym in asymptotes:
            ax.axvline(x=asym, color='red', linestyle='--', alpha=0.7, linewidth=2, label='Vertical Asymptote' if asym == asymptotes[0] else "")
        
        # Add holes
        for hole in features["holes"]:
            ax.plot(hole[0], hole[1], 'ko', markersize=8, markerfacecolor='white', markeredgecolor='black', markeredgewidth=2, label='Hole' if hole == features["holes"][0] else "")
        
        # Add x-intercepts
        for x_int in features["x_intercepts"]:
            ax.plot(x_int, 0, 'go', markersize=8, label='X-intercept' if x_int == features["x_intercepts"][0] else "")
        
        # Add y-intercept
        if features["y_intercept"] != 0:
            ax.plot(0, features["y_intercept"], 'ro', markersize=8, label='Y-intercept')
        
        # Styling
        ax.grid(True, alpha=0.3, color='white')
        ax.set_xlabel('x', fontsize=12, color='white')
        ax.set_ylabel('f(x)', fontsize=12, color='white')
        ax.set_title('Rational Function Graph', fontsize=14, color='white', fontweight='bold')
        
        # Set axis limits
        ax.set_xlim(-10, 10)
        ax.set_ylim(-20, 20)
        
        # Color the axes
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.tick_params(colors='white')
        
        # Add legend
        if len(ax.lines) > 0 or len([child for child in ax.get_children() if hasattr(child, 'get_label')]) > 0:
            ax.legend(loc='upper right', framealpha=0.8)
        
        # Display the plot
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Error creating graph: {str(e)}")
        # Create a simple fallback plot
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.text(0.5, 0.5, 'Graph could not be generated', 
                horizontalalignment='center', verticalalignment='center',
                transform=ax.transAxes, fontsize=16)
        st.pyplot(fig)
