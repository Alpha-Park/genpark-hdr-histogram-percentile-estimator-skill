# genpark-hdr-histogram-percentile-estimator-skill

[![CI](https://github.com/alphaparkinc/genpark-hdr-histogram-percentile-estimator-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-hdr-histogram-percentile-estimator-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> High Dynamic Range (HdrHistogram) latency percentile estimator tracking microsecond-to-hour request distributions with bounded precision error.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / Telemetry Source] -->|Trace Context / Span / Metric| Engine[genpark-hdr-histogram-percentile-estimator-skill]
    Engine --> ObservabilityCore[Tracing Propagator & Histogram Aggregator]
    ObservabilityCore --> Collector[(OpenTelemetry Collector / Dashboard)]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- Production-grade telemetry principles (W3C traceparent, HdrHistogram, t-Digest, Dapper sampling).
- Native Model Context Protocol (MCP) server support for AI agent observability.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-hdr-histogram-percentile-estimator-skill.git
cd genpark-hdr-histogram-percentile-estimator-skill
```

## Quickstart

```bash
python example_usage.py
```
