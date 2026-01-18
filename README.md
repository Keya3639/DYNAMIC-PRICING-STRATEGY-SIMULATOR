# DYNAMIC-PRICING-STRATEGY-SIMULATOR
The **Dynamic Pricing Strategy Simulator** is a machine-learning–powered web application that predicts real-time ride prices based on demand, supply, customer behavior, and ride conditions.Instead of fixed pricing, this system dynamically adjusts ride fares using surge logic and predictive modeling—similar to pricing strategies used by ride-hailing platforms like Uber and Ola.

This project is ideal for data scientists, business analysts, product managers, and students interested in pricing intelligence, demand–supply economics, and applied machine learning.
## Overview
The system uses a trained regression-based machine learning model stored as a .pkl file and deployed via an interactive Streamlit application.
It simulates real-world ride-booking scenarios by allowing users to input:

- Demand and supply conditions
- Ride timing and duration
- Customer loyalty
- Location and vehicle type
The application then predicts the final ride price, applies a surge multiplier, and visually compares base price vs surge price, making pricing behavior easy to understand and analyze.
## Tools and Technologies Used

- **Python:** Core programming language

- **Streamlit:** Interactive web-based UI

- **Scikit-learn:** Machine learning model for price prediction

- **Joblib:** Model loading and serialization

- **Pandas:** Feature engineering and data handling

- **Matplotlib:** Price comparison visualizations
## Why These Tools Were Selected

- Machine learning models capture complex pricing patterns better than static rules
- Streamlit enables rapid prototyping of pricing dashboards
- Pandas simplifies feature creation like demand–supply ratio
- Matplotlib provides clear visual comparison of pricing impact
- Joblib ensures fast inference without retraining
Together, these tools create a business-oriented, explainable pricing simulator.
## Features

- Real-time dynamic ride price prediction
- Demand–supply ratio calculation
- Surge multiplier logic (No / Mild / High / Extreme)
- Base price vs surge price comparison
- Customer loyalty-based pricing impact
- Peak-time pricing detection
- Interactive and clean UI
- Business-friendly pricing explanation
## How It Works

- User enters ride parameters:
   - Number of riders and drivers
   - Location category
   - Customer loyalty status
   - Ride timing and duration
   - Vehicle type and ratings

- System performs feature engineering:
   - Demand–Supply Ratio
   - Peak-Time indicator
   - ML model predicts surge-adjusted price
   - Surge multiplier is applied based on demand–supply imbalance

- System displays:
   - Base price
   - Final surge price
   - Surge level
   - Visual price comparison

- Explanation panel shows key pricing factors
## Advantages
- Simulates real-world pricing strategies
- Helps understand surge pricing mechanics
- Supports business and pricing decisions
- Interactive and easy-to-use
- Demonstrates applied ML in economics
- Suitable for demos and academic projects
## Limitations

- Pricing accuracy depends on training dataset
- Simulated environment may differ from live systems
- Does not account for real-time traffic or weather
- Surge logic is rule-based, not fully learned
- Not suitable for direct production deployment
## Real-Time Applications

- Ride-hailing platforms: Dynamic fare calculation
- Logistics services: Demand-based pricing
- E-commerce: Time-based and surge pricing
- Travel & mobility analytics
- Pricing strategy simulations
- Academic ML & business analytics projects
## Future Enhancements

- Real-time data integration
- Reinforcement learning for pricing optimization
- Profit vs demand elasticity analysis
- City-level heatmap pricing visualization
- A/B pricing strategy testing
- Cloud deployment (AWS / Azure)
- Admin dashboard for pricing control
- Multi-currency support
## Conclusion

The Dynamic Pricing Strategy Simulator demonstrates how machine learning and economic principles can be combined to build intelligent pricing systems.
By transforming demand and supply signals into transparent, data-driven pricing decisions, this project highlights the power of AI in modern digital marketplaces.
With future improvements, it can evolve into a robust pricing intelligence platform.

## Output
<img width="687" height="772" alt="Image" src="https://github.com/user-attachments/assets/f1464943-4a9e-46c1-9098-58553b5ac0a9" />

<img width="720" height="773" alt="Image" src="https://github.com/user-attachments/assets/8e3d50ce-0465-49ff-b16d-446ff06a1dfa" />

<img width="693" height="778" alt="Image" src="https://github.com/user-attachments/assets/e85aae96-c296-4455-9ff5-e91e057894cb" />
