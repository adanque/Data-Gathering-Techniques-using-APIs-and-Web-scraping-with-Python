



-- Analyis of Type of AirCraft
-- Top 10 Planes with the most flights with no survivors
select top 100
	 sub1.[Type of aircraft]
	,max(sub1.[PlaneAge]) PlaneAge
	,count(*) Number_of_Flights
	,avg(sub1.[Number On Board]) [Avg Number on Board]
	,avg(sub1.[Number of Survivors]) [Avg Survival]
	,sum(sub1.[Number On Board]) [Total Number on Board Flights]
from 
( 
	select a.[Crew on board]
		,a.[Pax on board]
		,a.[Crew fatalities]
		,a.[Pax fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) [Number On Board]
		,cast(a.[Total fatalities] as int) [Total fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) [Number of Survivors]
		,a.[Type of aircraft]
		,a.[Flight Type]
		,a.[Survivors]
		,cast(a.[PlaneAge] as int) [PlaneAge]
			from AviationFatalitiesDetails a (nolock)
				-- Invalid
				where 
					a.[Type of aircraft] like '%boeing%' 
				--a.[Crew on board] not in ('1920')
				--	and cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) > 0
				and cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) = 0
				and cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int)  > 20

--		order by cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) desc
) sub1
group by sub1.[Type of aircraft]
	order by count(*) desc


-- Analyis of Type of AirCraft
-- Top 10 Planes with the most flights with no survivors
select top 25
	 sub1.[Type of aircraft]
	,max(sub1.[PlaneAge]) PlaneAge
	,count(*) Number_of_Flights
	,avg(sub1.[Number On Board]) [Avg Number on Board]
	,avg(sub1.[Number of Survivors]) [Avg Survival]
	,sum(sub1.[Number On Board]) [Total Number on Board Flights]
	,avg(sub1.[Number of Survivors])/ cast(avg(sub1.[Number On Board]) as float) Survival_Rate
from 
( 
	select a.[Crew on board]
		,a.[Pax on board]
		,a.[Crew fatalities]
		,a.[Pax fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) [Number On Board]
		,cast(a.[Total fatalities] as int) [Total fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) [Number of Survivors]
		,a.[Type of aircraft]
		,a.[Flight Type]
		,a.[Survivors]
		,cast(a.[PlaneAge] as int) [PlaneAge]
			from AviationFatalitiesDetails a (nolock)
				-- Invalid
				where 
				a.[Crew on board] not in ('1920')
					and a.[Type of aircraft] like '%boeing%'
					and cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) > 0
					and cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int)  > 20
					and cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) <> 0
					and cast(a.[Crew on board] as int)  <> 0
					and cast(a.[Pax on board] as int)  <> 0
					and cast(a.[Total fatalities] as int)  <> 0

--				cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) = 0
--		order by cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) desc
) sub1
where sub1.[Number On Board] <> 0
group by sub1.[Type of aircraft]
	order by 
		avg(sub1.[Number of Survivors])/ cast(avg(sub1.[Number On Board]) as float)  desc
		,count(*) desc
		




-- Analyis of Type of AirCraft
select top 10
	 sub1.[Type of aircraft]
	,max(sub1.[PlaneAge]) PlaneAge
	,sum(sub1.[Number of Survivors]) [Total Number of Survivors]
	,sum(sub1.[Number On Board]) [Total Number on Board Flights]
	,count(*) Flights_with_survivors
	,avg(sub1.[Number of Survivors])/ cast(avg(sub1.[Number On Board]) as float)
from 
( 
	select a.[Crew on board]
		,a.[Pax on board]
		,a.[Crew fatalities]
		,a.[Pax fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) [Number On Board]
		,cast(a.[Total fatalities] as int) [Total fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) [Number of Survivors]
		,a.[Type of aircraft]
		,a.[Flight Type]
		,a.[Survivors]
		,cast(a.[PlaneAge] as int) [PlaneAge]
			from AviationFatalitiesDetails a (nolock)
				-- Invalid
				where a.[Crew on board] not in ('1920')
					and cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) > 0
--		order by cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) desc
) sub1
group by sub1.[Type of aircraft]
	order by count(*) desc






-- Age of Plane Analysis.
select
	 sub1.[Operator]
	,max(sub1.[PlaneAge]) PlaneAge
	,sum(sub1.[Number of Survivors]) [Total Number of Survivors]
	,sum(sub1.[Number On Board]) [Total Number on Board Flights]
	,count(*) Flights_with_survivors
from 
( 
	select a.[Crew on board]
		,a.[Pax on board]
		,a.[Crew fatalities]
		,a.[Pax fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) [Number On Board]
		,cast(a.[Total fatalities] as int) [Total fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) [Number of Survivors]
		,a.[Type of aircraft]
		,a.[Flight Type]
		,a.[Survivors]
		,a.[Operator]
		,cast(a.[PlaneAge] as int) [PlaneAge]
			from AviationFatalitiesDetails a (nolock)
				-- Invalid
				where a.[Crew on board] not in ('1920')
					and cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) > 0
--		order by cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) desc
) sub1
group by sub1.[Operator]
	order by count(*) desc



-- Analyis of Type of AirCraft
select
	 sub1.[Type of aircraft]
	,max(sub1.[PlaneAge]) PlaneAge
	,sum(sub1.[Number of Survivors]) [Total Number of Survivors]
	,sum(sub1.[Number On Board]) [Total Number on Board Flights]
	,count(*) Flights_with_survivors
from 
( 
	select a.[Crew on board]
		,a.[Pax on board]
		,a.[Crew fatalities]
		,a.[Pax fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) [Number On Board]
		,cast(a.[Total fatalities] as int) [Total fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) [Number of Survivors]
		,a.[Type of aircraft]
		,a.[Flight Type]
		,a.[Survivors]
		,cast(a.[PlaneAge] as int) [PlaneAge]
			from AviationFatalitiesDetails a (nolock)
				-- Invalid
				where a.[Crew on board] not in ('1920')
					and cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) > 0
--		order by cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) desc
) sub1
group by sub1.[Type of aircraft]
	order by count(*) desc


-- Analyis of Type of AirCraft
select
	 sub1.[Type of aircraft]
	,max(sub1.[PlaneAge]) PlaneAge
	,sum(sub1.[Number of Survivors]) [Total Number of Survivors]
	,sum(sub1.[Number On Board]) [Total Number on Board Flights]
	,count(*) Flights_with_survivors
from 
( 
	select a.[Crew on board]
		,a.[Pax on board]
		,a.[Crew fatalities]
		,a.[Pax fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) [Number On Board]
		,cast(a.[Total fatalities] as int) [Total fatalities]
		,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) [Number of Survivors]
		,a.[Type of aircraft]
		,a.[Flight Type]
		,a.[Survivors]
		,cast(a.[PlaneAge] as int) [PlaneAge]
			from AviationFatalitiesDetails a (nolock)
				-- Invalid
				where a.[Crew on board] not in ('1920')
					and cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) > 0
--		order by cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) desc
) sub1
group by sub1.[Type of aircraft]
	order by count(*) desc


select
	 a.[Type of aircraft]
	,min(a.[Crew on board]) min_crew
	,max(a.[Crew on board]) max_crew
	,min(cast(a.[Total fatalities] as int) )
	,max(cast(a.[Total fatalities] as int) )
	from AviationFatalitiesDetails a (nolock)
		where a.[Crew on board] <> 0
group by a.[Type of aircraft]

select
	*	from AviationFatalitiesDetails a (nolock)
		where a.[Crew on board] = 0


-- Does the number of crew members affect the survival rate.
select
	 a.[Type of aircraft]
	,a.[FlightDate]
	,cast(a.[Crew on board] as int) [Crew on board]
	,cast(a.[Pax on board] as int) [Pax on board]
	,cast(a.[Pax fatalities] as int) [Pax fatalities]
	,cast(a.[Total fatalities] as int) [Total fatalities]
	from AviationFatalitiesDetails a (nolock)
		where a.[Crew on board] <> 0
-- group by a.[Type of aircraft]



/*
select a.[Crew on board]
	,a.[Pax on board]
	,a.[Crew fatalities]
	,a.[Pax fatalities]
	,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) [Number On Board]
	,cast(a.[Total fatalities] as int) [Total fatalities]
	,cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) [Number of Survivors]
	,a.[Type of aircraft]
	,a.[Flight Type]
	,a.[Survivors]
	,a.[PlaneAge]
		from AviationFatalitiesDetails a (nolock)
			-- Invalid
			where a.[Crew on board] not in ('1920')
	order by cast(a.[Crew on board] as int) + cast(a.[Pax on board] as int) - cast(a.[Total fatalities] as int) desc
*/