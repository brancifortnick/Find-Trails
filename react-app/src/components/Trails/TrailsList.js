import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { getAllTrails } from '../../store/trails';
import './TrailsList.css';

const TrailsList = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const trails = useSelector(state => state.trails.allTrails);
  const trailsArray = Object.values(trails);

  useEffect(() => {
    dispatch(getAllTrails());
  }, [dispatch]);

  const handleTrailClick = (trailId) => {
    history.push(`/trails/${trailId}`);
  };

  if (!trailsArray.length) {
    return (
      <div className="trails-list-container">
        <h1>Loading trails...</h1>
      </div>
    );
  }

  return (
    <div className="trails-list-container">
      <h1>Explore Trails</h1>
      <div className="trails-grid">
        {trailsArray.map(trail => (
          <div 
            key={trail.id} 
            className="trail-card"
            onClick={() => handleTrailClick(trail.id)}
          >
            <img 
              src={trail.image_url || `/assets/images/trail${trail.id}.jpg`}
              alt={trail.name}
              className="trail-card-image"
              onError={(e) => {
                e.target.onerror = null;
                e.target.src = 'https://via.placeholder.com/800x600/86C232/ffffff?text=Trail+Image';
              }}
            />
            
            <div className="trail-card-content">
              <div className="trail-card-header">
                <h2 className="trail-name">{trail.name}</h2>
                {trail.state && (
                  <span className="trail-state">{trail.state.state_code}</span>
                )}
              </div>
              
              <p className="trail-description">
                {trail.description?.substring(0, 150)}
                {trail.description?.length > 150 ? '...' : ''}
              </p>
              
              <div className="trail-info">
                <div className="trail-stat">
                  <span className="stat-label">Length:</span>
                  <span className="stat-value">{trail.length} miles</span>
                </div>
                <div className="trail-stat">
                  <span className="stat-label">Difficulty:</span>
                  <span className="stat-value">{trail.difficulty}/10</span>
                </div>
                {trail.cross_state && (
                  <span className="cross-state-badge">Cross-State Trail</span>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TrailsList;
