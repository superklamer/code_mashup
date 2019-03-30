package com.superlamer.weatherapp.weather;

import org.bson.Document;

public class Coord implements Documentable {
	
	private double lon;
	private double lat;
	
	public Coord() {}
	public Coord(double lon, double lat) {
		super();
		this.lon = lon;
		this.lat = lat;
	}

	public double getLon() {
		return lon;
	}

	public void setLon(double lon) {
		this.lon = lon;
	}

	public double getLat() {
		return lat;
	}

	public void setLat(double lat) {
		this.lat = lat;
	}
	@Override
	public String toString() {
		return "Coord [lon=" + lon + ", lat=" + lat + "]";
	}
	
	public Document toDocument() {
		return new Document("lon", lon)
				.append("lat", lat);	
	}
	

}
