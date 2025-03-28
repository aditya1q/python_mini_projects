# app.py
from flask import Flask, request, jsonify
from db import init_db
from slippage import calculate_slippage

app = Flask(__name__)
trades_collection = init_db()


@app.route('/add_trade', methods=['POST'])
def add_trade():
    try:
        data = request.get_json()
        required_fields = ['trade_id', 'signal_time', 'signal_price',
                           'execution_time', 'execution_price', 'trade_type']

        # Validate input
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Insert trade into MongoDB
        trades_collection.insert_one({
            "trade_id": data['trade_id'],
            "signal_time": data['signal_time'],
            "signal_price": float(data['signal_price']),
            "execution_time": data['execution_time'],
            "execution_price": float(data['execution_price']),
            "trade_type": data['trade_type']
        })
        return jsonify({"status": "Trade added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get slippage for a specific trade


@app.route('/slippage/<trade_id>', methods=['GET'])
def get_slippage(trade_id):
    try:
        trade = trades_collection.find_one({"trade_id": trade_id})
        if trade:
            slippage = calculate_slippage(
                trade['signal_price'],
                trade['execution_price'],
                trade['trade_type']
            )
            return jsonify({
                "trade_id": trade_id,
                "signal_price": trade['signal_price'],
                "execution_price": trade['execution_price'],
                "slippage": slippage
            })
        return jsonify({"error": "Trade not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get average slippage (optional)


@app.route('/average_slippage', methods=['GET'])
def get_average_slippage():
    try:
        trades = list(trades_collection.find())
        if not trades:
            return jsonify({"error": "No trades found"}), 404

        total_absolute = 0
        total_percentage = 0
        count = 0

        for trade in trades:
            slippage = calculate_slippage(
                trade['signal_price'],
                trade['execution_price'],
                trade['trade_type']
            )
            total_absolute += slippage['absolute_slippage']
            total_percentage += slippage['percentage_slippage']
            count += 1

        return jsonify({
            "average_absolute_slippage": round(total_absolute / count, 2),
            "average_percentage_slippage": round(total_percentage / count, 2),
            "total_trades": count
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
